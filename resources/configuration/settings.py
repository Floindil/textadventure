from dotenv import load_dotenv
import os

load_dotenv()

rootconfig = {
    'name' : os.getenv('Gamename'),
    'width' : os.getenv('Rootwidth'),
    'height' : os.getenv('Rootheight')
}