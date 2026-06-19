# ------------------- ЗАПУСК ПРОГРАММЫ -------------------
from ui import show_menu, show_test_data
from report import generate_report

def main():
    while True:
        show_menu()
        choice = input("\nВведите номер действия: ").strip()

        if choice == "1":
            generate_report()

        elif choice == "2":
            show_test_data()

        elif choice == "0":
            print("─" * 80)
            print("До свидания!")
            break

        else:
            print("Неверный ввод. Пожалуйста, введите 0, 1 или 2.")

if __name__ == "__main__":
    main()