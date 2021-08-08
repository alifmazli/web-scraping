from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    print("Put some skill you are not familiar with")
    unfamiliar_skill = input('> ')
    print(f"Filtering out '{unfamiliar_skill}'...")

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_day = job.find('span', class_='sim-posted').text
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']

        if unfamiliar_skill not in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Company Name: {company_name.strip()}")
                f.write(f"Skills: {skills.strip()}")
                f.write(f"More info: {more_info}")
            print(f"File saved: {index}")
            
    if __name__ == '__main__':
        while True:
            find_jobs()
            time_wait = 10
            print(f"Waiting {time_wait} minutes... ")
            time.sleep(time_wait * 60)


    
    
    # Some cool stuffs
    # soup = BeautifulSoup(content, 'lxml')
    # course_cards = soup.find_all('div', class_='card')
    # for course in course_cards:
    #     course_name = course.h5.text
    #     course_price = course.a.text.split()[-1]

    #     print(f'{course_name} costs {course_price}')

    # Print all instances of a specific tag
    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)