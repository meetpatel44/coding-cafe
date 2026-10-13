1\. `--global` means the name and email are saved in Git's global configuration and apply to all my repositories by default. If I leave it out, the settings apply only to the current repository.



2\. `ls -a` shows the hidden `.git` directory, which does not appear in a normal `ls` listing. It stores Git's repository metadata, configuration, commit history, and references.



3\. In my recorded `git status`, Git listed one untracked folder, `lab4/`. It contained `.gitignore`, `README.md`, and `notes.md`, which were not yet tracked by Git.



4\. After creating `.gitignore`, files and folders matching its rules, such as `.venv/`, `\_\_pycache\_\_/`, and `\*.pyc`, should disappear from the untracked list. My recorded output does not show whether any of these were present initially.



5\. `.gitignore` itself should be committed because it tells Git which files to ignore. Tracking it allows everyone working on the repository to use the same ignore rules.



6\. `README.md` moves from the untracked files section to the changes to be committed section after running `git add README.md`. This moves the file from the working directory into Git's staging area, ready for a commit.



7\. My commit `0c857cc` reported that three files changed, with 26 insertions. These were the three files added under `lab4/`.



8\. The first seven characters of a commit's hash form its short commit ID. They provide a convenient way to identify and refer to a specific commit in the repository's history.



9\. The four steps are edit the files, stage the changes with `git add`, save them with `git commit`, and inspect the history using `git log`. Repeating this cycle records each stage of the project's development.



10\. `README.md` has a special name because GitHub automatically displays it on the repository's front page. It introduces the project and helps visitors understand its purpose and contents.



11\. `gh auth login` authenticated me through my web browser and configured GitHub CLI to use my GitHub credentials. This allows Git to authenticate pushes without asking for my account password each time.



12\. The repository's front page displays `README.md` as formatted Markdown. GitHub automatically renders this file because it is the standard introductory document for a repository.



13\. No, pushing did not change my local commit history. It uploaded my existing commits to GitHub, and `origin/main` now points to the same latest commit as my local `main` branch.



14\. A private repository exists on GitHub but can only be accessed by its owner and authorized collaborators. A repository that does not exist on GitHub has no hosted repository page or remote copy for collaborators to access.

