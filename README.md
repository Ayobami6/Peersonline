![Languages](https://img.shields.io/github/languages/top/Ayobami6/Peersonline)
![GitHub repo size](https://img.shields.io/github/repo-size/Ayobami6/Peersonline)
![GitHub issues](https://img.shields.io/github/issues/Ayobami6/Peersonline)
![GitHub closed issues](https://img.shields.io/github/issues-closed/Ayobami6/Peersonline)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Ayobami6/Peersonline)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/Ayobami6/Peersonline)
![GitHub](https://img.shields.io/github/license/Ayobami6/Peersonline)
![GitHub Repo stars](https://img.shields.io/github/stars/Ayobami6/Peersonline?style=social)
![GitHub forks](https://img.shields.io/github/forks/Ayobami6/Peersonline?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/Ayobami6/Peersonline)

Peers is a website that helps Alx Students of software engineering learn better, faster and do hard stuffs easily with colleagues and peers of the same cohort and different cohorts

Peers features are;

- Learn: This is a feature that allows student to learn with colleagues and peers on different tasks
- Mentor: This is a feature where peers can register to mentor others on a particular concept they want to talk about and teach, when a mentor register to mentor, all members of peers gets notified of the new mentor session.
- Ask gpt: This feature allows members of peers to ask chat gpt for advice on anything relating to software engineering alone, anything aside that gpt won't respond with what they expect.
- Post: This features allows members to post questions, articles, react to posts and comments
  and more.

## Challenge Statement:
- Problem intended to solve
Student not being able to schedule an organized PLD sessions where all members are active
- Problem not intended to solve:
Project will not solve student personal issues of not being able to learn with colleagues
- Project Users:
Students of ALX SE
Project is only relevant to the student of ALX SE

## Risks:
### Technical Risks:
- Compatibility Issues: Website not being compatible with different browsers; Safeguards: Will be leveraging the website can I use to help determine tools and libraries to use for the frontend development.
- Performance Problem: Slow loading times; Safeguards; Monitoring the server loads, load balancing the servers and also writing efficient code to improve performance
- Integration Difficulties: Integrating third party services or APIs  could be tricky due to compatibility issues or lack of good documentations; Safeguards: ensuring third party services or APIs has a proper documentation or tutorial for easy integration.
### Non-technical Risks:
Resource Constraint: Limited timeframes; Safeguards: effective time management




## Infrastructure:
- Strategy for deployment: CD using docker build, push and deploy github action
Will populate app with data by consuming APIs and querying the database:
- Tools for automation: Jenkins, Dango CI using pycodestyle action for coding style and pytest automation to test all test files on every push and pull request on github.


## Project Setup

<details>
<summary>
Steps
</summary>

- Create a folder with name peers on your local machine

```bash
mkdir peers
cd peers
git clone <url> .
```

- Create virtual environment for linux and MacOX

```bash
python3 -m venv venv
```

- Activate venv

```bash
. venv/bin/activate
```

for Windows

```bash
> mkdir peers
> cd peers
> py -3 -m venv venv
```

Activate for Windows

```bash
venv\Scripts\activate
```

- Install all project dependecies

```bash
pip install -r requirements.txt
```

- Create `.env` file inside the root of peers to store your OpenAI Api
  Or run

```bash
cp .env.example .env
```

then open the `.env` file to update your chatgpt api key

- Test the app from your local machine

Run

```bash
python manage.py runserver
```

Then open the generated port and host with your web browser with localhost/home

Like this

```
http://127.0.0.1:8000/home
```

If you encouter an issue setting up
create an Issue [here](https://github.com/Ayobami6/Peersonline/issues)

</details>

## Project Tools

- Python django
- Boostrap
- RDMS (Postgresql or Mysql or Sqlite)
- Html and Css
- FontAwesome Icons
- Docker for containerization
- Github Actions for CI
- Github Projects for Project management
- Github Discussions
- Chatgpt Api
- Pytest for unit testing
- Pycodestyle for python code style

## Project Resources

- [Django-guide-pdf](https://drive.google.com/file/d/1untLdjlgNQJdKIM9RzpwLEgMOEwTQc3l/view?usp=share_link)
- [Boostrap](https://www.freecodecamp.org/learn/front-end-development-libraries/)
- [Html-Css](https://www.freecodecamp.org/learn/2022/responsive-web-design/)

## Development environmennt Code Linter and Formatter tools tools recommendations

- Pycodestyle
- Prettier Formatter
- AutoPep8 Formatter

