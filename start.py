import os
from streamlit.web import bootstrap

if __name__ == "__main__":
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "false"
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    bootstrap.run("app.py", False, ["--server.port", "8501"], flag_options={})
