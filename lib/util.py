def try_load_dotenv():
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass
