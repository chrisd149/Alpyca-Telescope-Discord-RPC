from alpaca import Telescope
from pypresence import Presence
import time
import dotenv
import os

# Load env stuff
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

client_id = os.environ["discord-id"]
RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop

# Initialize a Telescope object, which is used for API calls
t = Telescope(os.environ["ip-address"], 0)

# Used to return elapsed time
start = int(time.time())

# Loop for the rest of the program
while True:
    # Checks status of telescope
    if t.slewing() is True:  # Telescope is moving to a target
        status = "Slewing to Target"
    elif t.tracking() is True:  # Telescope is tracking
        status = "Sidereal Tracking"
    else:  # Telescope is likely not doing anything
        status = "Idle"

    # Updates Discord status
    RPC.update(state=f"Current Status: {status}",
               details=f"RA: {round(t.rightascension(), 4)} | DEC: {round(t.declination(), 4)}",
               large_image='moon',
               large_text='hello :3',
               start=start)
    # Note: RA and DEC are coordinates for astronomical objects
    time.sleep(5)
