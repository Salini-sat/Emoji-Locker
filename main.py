import subprocess

def main():
    print("\n🎭 Welcome to Emoji Expression Locker 🔐")
    print("1. Register New User")
    print("2. Login with Expressions")
    print("3. Test Camera & Face Detection")
    print("0. Exit")

    choice = input("Enter your choice (0-3): ")

    if choice == '1':
        subprocess.run(["python", "register_user.py"])
    elif choice == '2':
        subprocess.run(["python", "authenticate_user.py"])
    elif choice == '3':
        subprocess.run(["python", "expression_detection.py"])
    elif choice == '0':
        print("Goodbye!")
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
