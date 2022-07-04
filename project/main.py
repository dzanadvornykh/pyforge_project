import argparse
import logging
from pathlib import Path


from apps.database import create_all_tables
from apps.getting_info import send_info_to_db
from apps.print_table import get_table


logging.basicConfig(
    filename=Path(__file__).parent / 'logs' / 'app.log', 
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--get_info', help='Put info about compound to database')
    parser.add_argument('--print', action="store_true", help='Print table with compounds')
    args = parser.parse_args()
    return args


def main():

    args = parse_args()
    
    create_all_tables()
    
    if args.get_info:
        send_info_to_db(args.get_info)
    elif args.print:
        table = get_table()
        print(table)


if __name__ == "__main__":
    main()
