## GitHub Branches

Branches allow you to organize work in a contained space. For our purposes, their most important feature is allowing you to make a pull request with only the specific changes you want to submit and *not* all the other things you may be experimenting with in your repository.

[Here's a more extended overview](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) of what branches are and how they work.

### Key Concepts
- Every repository or fork has a default branch ('main').
- You can make as many additional branches as you'd like.
- Commits are always made to a branch (even if it's 'main').
- When making a new branch in order to make a pull request to an upstream repository, I recommend using the 'main' branch of that upstream repository as the source for your new branch.

### Tips for Using Branches for Exercises
- Make a new branch for each exercise
- Make a copy of the exercise notebook, then rename the copy with your name as an underscored suffix (e.g., `exercise02_chester.ipynb`).
- Don't make changes unrelated to your exercise on the branch you set up for that exercise.
- If you accidentally make other changes, the easiest way to clean things up is be to make a new branch, then copy only the files you want to submit into that branch. You can temporarily copy them to the desktop as you move them between branches.
- Sync your branch before making a pull request.

### Detailed Steps for Doing Your Exercise on a Branch
1. Go to your fork of the course respository on the GitHub website (e.g., https://github.com/[your_username]/ursp688y_sp2025).
2. In the upper-left, click where it says "1 Branch" or "[n] Branches" to open branches page.
3. Click the green "New branch" button in the upper left.
4. Write a name for your new branch (e.g., "exercise-2").
5. Choose "ncsg/ursp688y_sp2025" as the source and "main" as the source branch. This will ensure your branch starts out being in sync with the course respository, reducing the likelihood of a conflict when you make a pull request.
6. Open GitHub Desktop and navigate to the clone of your fork.
7. Fetch from the origin, which will sync your new branch.
8. Select your new branch from the "Current Branch" dropdown at the center-top of the GitHub Desktop window
9. If you have uncommitted changes on your current branch (e.g., you may have been working on your exercise 2 notebook but hadn't yet committed the changes) a dialog will pop up asking if you want to keep the changes on 'main' or move them to your new branch. I recommend only moving changes if you're confident they're related to the purpose of your new branch.
10. Once you're on the new branch, work on your code (e.g., open Jupyter Lab and write code, copy and move files, etc.). Make commits to your new branch. You can keep and come back to this branch for however long you're working on the exercise.
    - When you have a branch selected, the Windows Explorer, Mac Finder, or file navigator in Jupyter Lab automatically show the state of that branch within the cloned directory. You are working with the *version* of the repository/fork stored in the selected branch.
    - ***Note: Don't delete the template exercise notebook. Instead, make a copy of it, then rename the copy with your name as an underscored suffix (e.g., `exercise02_chester.ipynb`)***
    - If you previously committed changes related to the exercise in the 'main' branch, I recommend going back to 'main', copying any new/changed files to your Desktop, then going back to your new branch and copying the files into it. Then commit them on the new branch.
11. When you're done coding and ready to make a pull request from your branch, push and fetch the origin a final time to make sure everything is in sync between your computer and the cloud.
12. Go to your fork on GitHub.com.
13. Go to the branches page and click on your branch.
14. Click "Sync fork" to make sure it's up-to-date with upstream course repository.
15. Click "Contribute" and "Open pull request".
16. Scroll down and make sure that only the files you intended to include in the pull request are included.
17. Add a title and description. Click "Create pull request".
