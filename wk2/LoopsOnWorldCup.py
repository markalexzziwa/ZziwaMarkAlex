print("=== World Cup 2026 Winner Simulator ===")

while True:
    user_input = input("\nEnter a country name to check its 2026 World Cup prediction (or type 'exit'): ").strip()
    if user_input.lower() == 'exit':
        print("Exiting simulator. Goodbye!")
        break
        
    if not user_input:
        print("Error: Input cannot be empty.")
        continue
    if user_input.lower() == "uganda":
        pass
    if user_input.lower() in ["canada", "mexico", "usa"]:
        print(f"🔮 Prediction: As a co-host, {user_input} has a massive home advantage to win World Cup 2026!")
    else:
        print(f"🔮 Prediction: {user_input} has a solid 2026 strategy and strong roster depth to claim the trophy!")
