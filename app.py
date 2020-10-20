from dreamparser import DreamParser
from database import db, Dream


def main():
    dream_parser = DreamParser(1)
    
    dream_html = dream_parser.get_next_dream_html()
    dreams = []
    
    while dream_html:
        dreams.append(dream_parser.get_dream(dream_html))
        print(dreams[-1]["id"], dreams[-1]['title'])

        dream_html = dream_parser.get_next_dream_html()
    
    db.connect()
    db.create_tables([Dream])
    
    with db.atomic():
        Dream.insert_many(dreams).execute()


if __name__ == '__main__':
    main()
