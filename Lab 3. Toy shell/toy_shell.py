#!/usr/bin/env python3
import os
import time
from datetime import datetime


def list_items_older_than(date_input):
    try:
        target_date = datetime.strptime(
            date_input, "%Y-%m-%d"
        ).timestamp()

        items = os.listdir(".")

        found = False

        for item in items:
            if item == ".git":
                continue

            item_path = os.path.join(".", item)

            if os.path.isdir(item_path) or os.path.isfile(item_path):
                stats = os.stat(item_path)

                creation_time = getattr(
                    stats, "st_birthtime", stats.st_ctime
                )

                if creation_time < target_date:
                    item_type = (
                        "Folder" if os.path.isdir(item_path) else "File"
                    )

                    formatted_time = time.strftime(
                        "%Y-%m-%d %H:%M:%S",
                        time.localtime(creation_time)
                    )

                    print(
                        f"{item} ({item_type}, "
                        f"Created: {formatted_time})"
                    )
                    found = True

        if not found:
            print("No files or folders found before this date.")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


def toy_shell():
    print("Toy Shell: List items older than a given date")
    print("Enter a date (YYYY-MM-DD) or type 'exit' to quit.")

    while True:
        try:
            command = input("toy-shell> ").strip()

            if command.lower() == "exit":
                print("Exiting toy shell.")
                break

            list_items_older_than(command)

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")


if __name__ == "__main__":
    toy_shell()

