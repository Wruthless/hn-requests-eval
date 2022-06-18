from operator import itemgetter
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

sub_ids = r.json()
sub_dicts = []

for sub_id in sub_ids[:30]:
    # Make separate API calls for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{sub_id}.json"
    r = requests.get(url)
    print(f"id: {sub_id}\tstatus:{r.status_code}")
    response_dict = r.json()
    
    sub_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={sub_id}",
        'comments': response_dict['descendants'],
    }
    
    sub_dicts.append(sub_dict)
    
sub_dicts = sorted(sub_dicts, key=itemgetter('comments'), reverse=True)

for sub_dict in sub_dicts:
    print(f"\nTitle: {sub_dict['title']}")
    print(f"Discussion link: {sub_dict['hn_link']}")
    print(f"Comments: {sub_dict['comments']}")