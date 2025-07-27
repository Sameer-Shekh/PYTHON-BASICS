file = open('youtube_manager.txt', 'w')


try:
    file.write("YouTube Manager Initialized\n")
    
finally:
    file.close()
    print("File closed successfully.")


with open('youtube_manager.txt', 'w') as file:
    content = file.write("chai aur python")
    print("File Content:\n", content)