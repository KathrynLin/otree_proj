#!/usr/bin/env python
"""
Simple calculator data export using SQLite directly
Exports data from BOTH quiz_low_four and public_goods_low_four apps
Usage: python export_calculator_simple.py
"""
import sqlite3
import csv
import json
from datetime import datetime


def export_calculator_data():
    """Export calculator data from SQLite database"""
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    all_submissions = []

    # Get calculator data from quiz_low_four app
    print("Fetching quiz_low_four calculator data...")
    cursor.execute("""
        SELECT
            s.code as session_code,
            p.code as participant_code,
            p.id_in_session as participant_id,
            'quiz' as app_name,
            1 as round_number,
            player.calculator_usage_log
        FROM quiz_low_four_player as player
        JOIN otree_participant as p ON player.participant_id = p.id
        JOIN otree_session as s ON p.session_id = s.id
        WHERE player.calculator_usage_log IS NOT NULL
          AND player.calculator_usage_log <> ''
    """)

    process_rows(cursor.fetchall(), all_submissions, 'quiz')

    # Get calculator data from public_goods_low_four app
    print("Fetching public_goods_low_four calculator data...")
    cursor.execute("""
        SELECT
            s.code as session_code,
            p.code as participant_code,
            p.id_in_session as participant_id,
            'public_goods' as app_name,
            player.round_number,
            player.calculator_usage_log
        FROM public_goods_low_four_player as player
        JOIN otree_participant as p ON player.participant_id = p.id
        JOIN otree_session as s ON p.session_id = s.id
        WHERE player.calculator_usage_log IS NOT NULL
          AND player.calculator_usage_log <> ''
    """)

    process_rows(cursor.fetchall(), all_submissions, 'public_goods')

    conn.close()

    # Export to CSV
    if all_submissions:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'calculator_submissions_{timestamp}.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['session_code', 'participant_code', 'participant_id', 'app_name',
                         'round_number', 'timestamp', 'page_url',
                         'member1', 'member2', 'member3', 'my_investment']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_submissions)

        print(f"\n✅ Exported {len(all_submissions)} calculator submissions to: {filename}")
    else:
        print("\n⚠️  No calculator submissions found")
        print("\nTo collect calculator data:")
        print("  1. Use the calculator and click Submit")
        print("  2. Fill in your contribution and click Next")
        print("  3. The data will be saved when you submit the form")


def process_rows(rows, all_submissions, app_name):
    """Process database rows and extract calculator submissions"""
    print(f"  Found {len(rows)} records with calculator data in {app_name}")

    for session_code, participant_code, participant_id, app, round_number, calc_log in rows:
        try:
            # Parse JSON
            submissions = json.loads(calc_log)

            if not isinstance(submissions, list):
                continue

            for submission in submissions:
                all_submissions.append({
                    'session_code': session_code,
                    'participant_code': participant_code,
                    'participant_id': participant_id,
                    'app_name': app_name,
                    'round_number': round_number,
                    'timestamp': submission.get('timestamp', ''),
                    'page_url': submission.get('url', ''),
                    'member1': submission.get('member1', ''),
                    'member2': submission.get('member2', ''),
                    'member3': submission.get('member3', ''),
                    'my_investment': submission.get('my', ''),
                })
        except (json.JSONDecodeError, TypeError) as e:
            print(f"  ⚠️  Error parsing data for participant {participant_code}: {e}")


if __name__ == '__main__':
    export_calculator_data()
