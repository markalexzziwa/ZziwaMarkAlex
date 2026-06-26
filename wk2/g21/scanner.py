import sys
import os
import re
import json

# =========================================================================
# PERSON 1: The File Reader & Line Counter
# =========================================================================
class FileReader:
    @staticmethod
    def read_file(file_path):
        """Reads file line-by-line safely with UTF-8 encoding."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Target file path not found: {file_path}")
            
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()

    @staticmethod
    def count_metrics(all_lines, blank_lines_count, comment_lines_count):
        """Compiles standard file line telemetry."""
        total = len(all_lines)
        # Lines of code = total lines minus empty lines and pure comment lines
        loc = max(0, total - blank_lines_count - comment_lines_count)
        return total, loc


# =========================================================================
# PERSON 2: Regex/Logic for Finding Keywords (Complexity)
# =========================================================================
class ComplexityChecker:
    @staticmethod
    def count_keywords(code_lines):
        """Counts conditional statements and loop block controllers using word boundaries."""
        counts = {"if": 0, "elif": 0, "else": 0, "for": 0, "while": 0}
        keywords = counts.keys()
        
        for line in code_lines:
            for kw in keywords:
                # \b avoids false positives like matching "format" as "for"
                pattern = rf"\b{kw}\b"
                matches = re.findall(pattern, line)
                counts[kw] += len(matches)
        return counts


# =========================================================================
# PERSON 3: Comment Detection Logic (handling # and docstrings)
# =========================================================================
class CommentDetector:
    @staticmethod
    def analyze_comments(raw_lines):
        """Identifies pure blank lines, comments, docstrings, and clean code paths."""
        blank_count = 0
        comment_count = 0
        code_only_lines = []
        
        in_docstring = False
        docstring_char = None
        
        for line in raw_lines:
            stripped = line.strip()
            
            # Count blank lines
            if not stripped:
                blank_count += 1
                continue
                
            # Handle Multi-line Docstring boundaries
            if not in_docstring:
                if stripped.startswith('"""'):
                    in_docstring = True
                    docstring_char = '"""'
                    comment_count += 1
                    if stripped.endswith('"""') and len(stripped) > 3:
                        in_docstring = False
                    continue
                elif stripped.startswith("'''"):
                    in_docstring = True
                    docstring_char = "'''"
                    comment_count += 1
                    if stripped.endswith("'''") and len(stripped) > 3:
                        in_docstring = False
                    continue
            else:
                comment_count += 1
                if stripped.endswith(docstring_char):
                    in_docstring = False
                continue

            # Handle explicit single-line inline comments
            if stripped.startswith('#'):
                comment_count += 1
                continue
                
            # Handle partial inline comments (e.g., x = 5 # comment)
            if '#' in line:
                comment_count += 1
                code_part = line.split('#')[0]
                if code_part.strip():
                    code_only_lines.append(code_part)
                continue

            code_only_lines.append(line)
            
        return blank_count, comment_count, code_only_lines


# =========================================================================
# PERSON 4: Variable Extraction & Naming Rule Validator
# =========================================================================
class VariableValidator:
    @staticmethod
    def check_variables(raw_lines):
        """Finds items assigned with = and ensures they use snake_case formatting."""
        warnings = []
        snake_case_pattern = r"^[a-z0-9_]+$"
        
        for line_num, line in enumerate(raw_lines, 1):
            # Exclude logical operations or comparison boundaries (==, !=, <=, >=)
            if "=" in line and "==" not in line and "!=" not in line and "<=" not in line and ">=" not in line:
                left_side = line.split("=")[0].strip()
                
                # Extract words/variables to the left of the assignment operator
                vars_found = re.findall(r"\b[a-zA-Z0-9_]+\b", left_side)
                
                for var in vars_found:
                    # Filter out purely numeric entries or core structural words
                    if var.isdigit() or var in ["self", "if", "for", "while", "return"]:
                        continue
                        
                    # Check snake_case compliance rule
                    if not re.match(snake_case_pattern, var):
                        warnings.append(f"Line {line_num}: Variable '{var}' is not snake_case.")
                        
        return warnings


# =========================================================================
# PERSON 5: The Integrator
# =========================================================================
class SolutionIntegrator:
    def __init__(self, file_path):
        self.file_path = file_path

    def compile_metrics(self):
        """Coordinates metrics gathering across all roles and calculates score."""
        # 1. Fetch raw line data (Person 1)
        raw_lines = FileReader.read_file(self.file_path)
        
        # 2. Parse out blanks and comment layers (Person 3)
        blanks, comments, clean_code = CommentDetector.analyze_comments(raw_lines)
        
        # 3. Calculate finalized structural counters (Person 1)
        total, loc = FileReader.count_metrics(raw_lines, blanks, comments)
        
        # 4. Assess complexity keyword density (Person 2)
        complexity_data = ComplexityChecker.count_keywords(clean_code)
        
        # 5. Extract naming warnings (Person 4)
        naming_warnings = VariableValidator.check_variables(raw_lines)
        
        # 6. Calculate comment percentage ratio safely
        comment_ratio = round((comments / total) * 100, 2) if total > 0 else 0.0
        
        # 7. Calculate custom Developer Productivity Health Score
        score = 100 - (len(naming_warnings) * 2)  # Deduct 2 points per non-snake_case variable
        if sum(complexity_data.values()) > 15:    # Deduct 10 points for excessive keyword density
            score -= 10
        health_score = max(0, min(score, 100))

        # Compile final telemetry payload dictionary
        output_dict = {
            "total_lines": total,
            "blank_lines": blanks,
            "lines_of_code": loc,
            "comment_lines": comments,
            "comment_ratio_pct": comment_ratio,
            "complexity": complexity_data,
            "naming_warnings": naming_warnings,
            "health_score": health_score
        }
        
        return output_dict

    def print_formatted_output(self, stats_dict):
        """Prints compiled statistics to terminal as beautiful formatted JSON."""
        print(json.dumps(stats_dict, indent=4))


def main():
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <path_to_python_file.py>")
        sys.exit(1)
        
    target_file = sys.argv[1]
    integrator = SolutionIntegrator(target_file)
    
    try:
        results = integrator.compile_metrics()
        integrator.print_formatted_output(results)
    except Exception as e:
        error_payload = {"status": "Error", "message": str(e)}
        print(json.dumps(error_payload, indent=4))


if __name__ == "__main__":
    main()
