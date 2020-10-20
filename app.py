from dreamparser import DreamParser
from database import DataBase


def main():
    dream_base = DataBase()
    dream_parser = DreamParser(1)
    
    dream_html = dream_parser.get_next_dream_html()
    dreams = []
    
    while dream_html:
        dreams.append(dream_parser.get_dream(dream_html))
        print(dreams[-1]["id"], dreams[-1]['title'])

        dream_html = dream_parser.get_next_dream_html()
    
    dream_base.write(dreams)


if __name__ == '__main__':
    main()
