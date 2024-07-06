def try_load_dotenv():
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        print("failed to load dotenv")
