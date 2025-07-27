import json

def load_data():
    try:
        with open('youtube.text','r') as file:
            test =  json.load(file)
            # print(type(test)) <class 'list'>
            return test
    except FileNotFoundError:
        print("File not found. Initializing with an empty list.")
        return []
        

def save_data(videos):
    with open('youtube.text', 'w') as file:
        json.dump(videos, file)
        print("Data saved successfully.")

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos,start=1):
        print(f"{index}. content: {video['name']}, duration: {video['time']}.")
    # for vid in videos:
    #     print(f"content: {vid}.")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1<= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data(videos)
    else:
        print("Invalid index. No video updated.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index <= len(videos):
        # videos.pop(index - 1)
        # save_data(videos)
        del videos[index - 1]
        save_data(videos)
    else:
        print("Invalid index. No video deleted.")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting YouTube Manager.")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()