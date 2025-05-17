
from utility import (
    add_student, show_scores, update_score,
    get_average, get_top_student,delete_student,show_student, show_students_count
)


def main():
    while True:
        print("\n--- Student Score Manager ---")
        print("1. Add student")
        print("2. Show scores")
        print("3. Update score")
        print("4. Get average score")
        print("5. Get top student")
        print("6. Delete student")
        print("7. Show the score for a student")
        print("8. show the count of  students in a group")
        print("9. Exit")
        choice = input("Choose an option: ")


        #hahaahahha
#fkjlasd
        
        if choice == "1":
            group = input("Enter group name: ")
            name = input("Enter student name: ")
            subjects = input("Enter subjects (comma-separated): ").split(",")
            scores = {}
            for subject in subjects:
                subject = subject.strip()
                score = int(input(f"Score for {subject}: "))
                scores[subject] = score
            add_student(group, name, scores)

        elif choice == "2":
            group = input("Enter group name (leave empty for all): ").strip()
            show_scores(group if group else None)

        elif choice == "3":
            group = input("Enter group name: ")
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            score = int(input("Enter new score: "))
            update_score(group, name, subject, score)

        elif choice == "4":
            subject = input("Enter subject: ")
            group = input("Enter group name (leave empty for all): ").strip()
            get_average(subject, group if group else None)

        elif choice == "5":
            subject = input("Enter subject: ")
            group = input("Enter group name (leave empty for all): ").strip()
            get_top_student(subject, group if group else None)

        elif choice == "6":
            group = input("Enter group name: ")
            name = input("Enter student name: ")
            delete_student(group, name)

        elif choice == "7":
            group = input("Enter group name: ")
            name = input("Enter student name: ")
            show_student(group, name)

        elif choice == "8":
            group = input("Enter group name: ")
            show_students_count(group, )

        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
