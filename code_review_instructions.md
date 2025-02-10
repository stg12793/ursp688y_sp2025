GitHub has some terrific features for reviewing pull requests. Unfortunately, many of these features don't directly carry over to Jupyter Notebooks because of the complex structure in which they store information about cells, Markdown, etc.

As a workaround, we'll use an add-on app called GitNotebooks, which renders notebooks and allows you to make comments on individual lines, just like GitHub would for a non-notebook file.

To do a code review with GitNotebooks, make sure you are signed into GitHub with your browser, then go to:

[https://app.gitnotebooks.com/ncsg/ursp688y_sp2025/pulls](https://app.gitnotebooks.com/ncsg/ursp688y_sp2025/pulls)

1. Click on a pull request to begin reviewing it.

2. Wait for the notebook to render.

3. Click the blue [+] button to the left of a line of code on the right (green) side of the split "diff" screen. If the file you're reviewing is too large, it may only show the green side. The left (red) side shows the previous state of the code, for comparison.

4. Enter a comment and click [Add comment].

5. Enter more comments.

6. Click on [Review changes] in the upper right.

7. Enter a final comment if you want to sum things up.

8. Click [Submit review].

Here are some guidelines for code review, adapted from John Ousterhout’s Software Design Studio at Stanford University:

- Write approximately 5-15 comments, depending on code complexity and issues/strengths.
- Focus on red flags, including issues with flow, logic, documentation.
- Is the code easily understandable? Could you use or adapt it? Identify the most complicated parts.
- How effective are variables and functions? Too generalized? Not generalized enough?