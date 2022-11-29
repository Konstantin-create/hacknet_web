from bs4 import BeautifulSoup
from datetime import datetime
from app import db, web_site_folder


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    text = db.Column(db.String(120), nullable=False)
    tags = db.Column(db.String(12000), nullable=False)
    preview_img = db.Column(db.String, nullable=False)
    main_img = db.Column(db.String, nullable=False)
    views = db.Column(db.Integer, default=0)
    time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def get_short_description(self) -> str:
        """Function to get short description for post"""

        with open(f'{web_site_folder}/templates/temp/posts/{self.id}.html', 'r') as file:
            full_text = file.read()
        soup = BeautifulSoup(full_text, 'html.parser')
        p_tags = soup.find_all('p')
        return p_tags[0]

    def __repr__(self):
        return f'<Post: {self.id} | {self.header}>'
