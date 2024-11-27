# Function to filter bad words
def filter_bad_words(message, bad_words):
    words = message.split()  # Split the message into words
    filtered_words = []
    
    for word in words:
        # Replace bad words with a smile emoji
        if word.lower() in bad_words:
            filtered_words.append('😊')
        else:
            filtered_words.append(word)
    
    return ' '.join(filtered_words)  # Join the words back into a string

def main():
    # List of bad words
    bad_words = ['badword1', 'badword2', 'badword3']  # Replace with your own list of bad words

    print("Welcome to the chat program!")
    print("Type 'exit' to leave the chat.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break

        # Filter bad words
        filtered_message = filter_bad_words(user_input, bad_words)

        # Display the filtered message to the receiver
        print("Filtered: " + filtered_message)

        # Optional: Display the original message to the sender for reference
        # print("You (original): " + user_input)  # Uncomment to show the original message

if __name__ == "__main__":
    main()
