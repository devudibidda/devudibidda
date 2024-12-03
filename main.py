from telethon import TelegramClient, events

# Replace these values with your own
api_id = '1065341'
api_hash = '6ed21c43ba59b42b26ffd4165586e400'
source_channels = [-1001201589228, -1001391583159]  # List of source channel IDs
target_channel_id = 5984595326  # Replace with your target group ID
phone_number = '917013036598'
password = 'Vuntay@9'  # Replace with your 2FA password

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    """Handles new messages from the source channels."""
    
    # Get the input entity for the target group
    target_entity = await client.get_input_entity(target_channel_id)
    
    # Forward the message to the target group
    await client.send_message(target_entity, event.message)

try:
    # Start the client
    client.start(phone=phone_number, password=password)
    print("Client is running...")
    client.run_until_disconnected()
except Exception as e:
    print(f"An error occurred: {e}")