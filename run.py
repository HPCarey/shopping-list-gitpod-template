import os
from shoppinglist import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        # client_id=os.environ.get("CLIENT_ID"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
    )
