Here are detailed steps for retrieving content from GitHub and making a pull request to submit new content (such as an exercise).

It looks complicated, and there are a few places where the details matter. But once you do it several times it will feel more natural.

These instructions assume that you have already made a GitHub account and installed GitHub Desktop on your computer.

#### Part 0: Fork the course repo at GitHub.com (only the first time)
0. Fork the [`ncsg/ursp688y_sp2025`](https://github.com/ncsg/ursp688y_sp2025) repo to your own account at GitHub.com.

#### Part 1: Clone your fork in GitHub Desktop (only the first time)
1. Go to File -> Clone Repository
2. Click on your fork of the repository in the GitHub.com list (`yourname/ursp688y_sp2025`)
3. Select "To contribute to the parent project" in the dialog about you're planning to use this fork.

#### Part 2: Fetch, edit, commit, and push your fork
4. GitHub Desktop: In your cloned fork, fetch from the origin (`Fetch origin`) to ensure your version is up-to-date
5. JupyterLab: Write code, add data, etc. (***see JupyterLabInstructions.md for more details***)
6. GitHub Desktop: Commit each major change
7. GitHub Desktop: Periodically push to the origin (`Push origin`)
8. Rinse and repeat...

#### Part 3: Make a pull request to the course repo
9. In your fork on the GitHub website, navigate to the root directory
9. `Sync fork` to make sure your new additions are the only differences between your fork and the course repo.
    - If prompted, DON'T click the red `Discard commits` button to delete the file you just added; click the green `Update branch` button to sync everything else that might have changed.
10. `Contribute` (to the left of `Sync Fork`), and `Open pull request`.
11. Add a short but meaningful title for your pull request (e.g., submitting exercise 1).
12. (optional) Add a description if there's something additional you'd like me (and others) to know about your submission.
13. Click `Create pull request` at the bottom.

#### 🙌 Congrats!