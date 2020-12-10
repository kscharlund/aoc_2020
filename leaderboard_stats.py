from datetime import timedelta, datetime, timezone
import json
import sys


def get_user_star_timestamps(data):
    user_star_timestamps = {}
    for user in data['members'].values():
        name = user['name']
        user_star_timestamps[name] = {}
        completions = user['completion_day_level']
        for problem in sorted(completions, key=int):
            tss = [int(completions[problem]['1']['get_star_ts'])]
            if '2' in completions[problem]:
                tss.append(int(completions[problem]['2']['get_star_ts']))
            user_star_timestamps[name][int(problem)] = tss
    return user_star_timestamps


def main():
    if len(sys.argv) > 1:
        json_file = open(sys.argv[1])
    else:
        json_file = sys.stdin
    user_star_timestamps = get_user_star_timestamps(json.load(json_file))
    fastest_first_star = None
    fastest_second_star = None
    for user, problems in user_star_timestamps.items():
        print(user)
        for problem, timestamps in problems.items():
            cet = timezone(timedelta(hours=1))
            problem_open = datetime(2020, 12, problem, 6, 0, 0, tzinfo=cet)
            first_star = datetime.fromtimestamp(timestamps[0], tz=cet)
            to_first = first_star - problem_open

            if len(timestamps) > 1:
                second_star = datetime.fromtimestamp(timestamps[1], tz=cet)
                to_second = second_star - first_star
            else:
                to_second = None

            print(f'{problem:02d}: {to_first} from open to first star'
                  + (f', {to_second} from first to second star' if to_second else '.'))

            if fastest_first_star is None or to_first < fastest_first_star[0]:
                fastest_first_star = (to_first, problem, user)
            if fastest_second_star is None or (to_second is not None
                                               and to_second < fastest_second_star[0]):
                fastest_second_star = (to_second, problem, user)

        print()

    print(f'Fastest first star: 2020-12-{fastest_first_star[1]:02} in {fastest_first_star[0]} by {fastest_first_star[2]}')
    print(f'Fastest second star: 2020-12-{fastest_second_star[1]:02} in {fastest_second_star[0]} by {fastest_second_star[2]}')

if __name__ == '__main__':
    main()
