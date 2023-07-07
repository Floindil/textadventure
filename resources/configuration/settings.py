from dotenv import load_dotenv
import os

load_dotenv()

rootsize = {
    'width' : os.getenv('rootwidth'),
    'height' : os.getenv('rootheight')
}