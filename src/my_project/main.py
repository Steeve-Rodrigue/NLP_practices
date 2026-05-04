from pathlib import Path

def main():
    output_file = Path("outputs/result.txt")
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w") as f:
        f.write("Hello from the project!")

    print("Execution finished. Output saved.")

if __name__ == "__main__":
    main()