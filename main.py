from gui import start_gui

if __name__ == "__main__":
    try:
        start_gui()
    except Exception as e:
        print(f"An error occurred: {e}")