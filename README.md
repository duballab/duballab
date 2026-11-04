# Dubal Lab website

This is the source of the Dubal Lab website. It is a small, fast website built with [Hugo](https://gohugo.io), a tool that turns plain text files into web pages. There is no database and no passwords to maintain: every page is a text file in this project.

This guide assumes **nothing is installed on your computer and you have no accounts yet**. It takes you from zero to a working, editable, published website. Read sections 1 to 3 once. After that, you only need section 4 (or 5) for everyday work.

## Contents

1. [How it fits together](#1-how-it-fits-together)
2. [Starting from scratch: accounts and getting the project](#2-starting-from-scratch-accounts-and-getting-the-project)
3. [Publishing the site with Cloudflare](#3-publishing-the-site-with-cloudflare)
4. [Everyday editing in the browser (no installs)](#4-everyday-editing-in-the-browser-no-installs)
5. [Editing on your own computer (optional)](#5-editing-on-your-own-computer-optional)
6. [How to write the content files](#6-how-to-write-the-content-files)
7. [Adding pictures](#7-adding-pictures)
8. [Checking your work](#8-checking-your-work)
9. [Troubleshooting](#9-troubleshooting)
10. [What is where](#10-what-is-where)

---

## 1. How it fits together

| Place | What it is | Account needed |
|---|---|---|
| **GitHub** | A website that stores the project files and remembers every past version. This is the "master copy". | Yes, free |
| **Cloudflare** | Hosts the live website. Each time the master copy on GitHub changes, Cloudflare rebuilds and publishes the site automatically, in about two minutes. | Yes, free |
| **Pages CMS** *(optional)* | A friendly online editor with simple forms for people, publications and news. | Uses your GitHub login |

The flow is always the same: **you change a file on GitHub, and the live site updates by itself.** If a change contains a mistake that stops the site from building, Cloudflare keeps showing the last good version, so a typo cannot take the site down.

You do not have to install anything on your computer for ordinary editing (section 4). Section 5 describes the optional, more advanced way of working locally.

---

## 2. Starting from scratch: accounts and getting the project

Do this once. Whoever owns the website should do it, using a shared lab email address if possible, so the website does not depend on one person's login.

### 2.1 Create a GitHub account

1. Go to [github.com](https://github.com) and choose **Sign up**.
2. Follow the steps. Use the lab's email address if there is one.
3. Optional but recommended: switch on two-factor login under **Settings, then Password and authentication**.

### 2.2 Get the project into your GitHub account

The project currently lives in the repository **`adamcseresznye/duballab`**. You need a copy that belongs to the lab. Pick **one** of these:

**Option A: transfer ownership (cleanest).** The current owner opens the repository on GitHub, chooses **Settings**, scrolls to **Danger Zone**, chooses **Transfer**, and types the new owner's GitHub username. The new owner accepts the invitation sent by email. History is kept, and nothing needs to be copied.

**Option B: the new owner gets a copy.**
1. The current owner invites the new owner under the repository's **Settings, then Collaborators**.
2. The new owner accepts the invitation, opens the repository, and chooses **Fork** (top right) to make a copy under their own account.
3. Later, the original repository can be deleted.

**Option C: start from a downloaded folder.**
1. On the repository page choose **Code, then Download ZIP**, and unzip it.
2. On GitHub choose **+ (top right), then New repository**. Name it `duballab`, keep it empty (do not add a README), and create it.
3. On the new empty repository page choose **uploading an existing file**. Drag in the **contents** of the unzipped folder (the folders `content`, `layouts`, `static`, `tests` and the loose files). Drag the contents, not the outer folder. Hidden files such as `.gitignore` and `.pages.yml` are easy to miss: make sure they are included. If your upload is refused for having too many files, upload one folder at a time.
4. Choose **Commit changes**.

In all three cases you end with a repository in the lab's own GitHub account. The rest of this guide calls it **your repository**.

---

## 3. Publishing the site with Cloudflare

Do this once.

### 3.1 Create a Cloudflare account

Go to [dash.cloudflare.com](https://dash.cloudflare.com) and sign up (free).

### 3.2 Connect your repository

1. In the Cloudflare dashboard open **Workers & Pages**.
2. Choose **Create**, then **Connect to Git** (wording may vary slightly), and allow Cloudflare to access GitHub.
3. Select your `duballab` repository.
4. Enter these settings exactly:

   | Setting | Value |
   |---|---|
   | Build command | `hugo --minify` |
   | Deploy command | `npx wrangler deploy` |
   | Non-production branch deploy command | `npx wrangler versions upload` |
   | Root directory | *(leave empty)* |

5. Add an **environment variable** named `HUGO_VERSION` with the value `0.169.0`. Cloudflare needs it to know which Hugo to use.
6. Choose **Save and Deploy**. After a minute or two you get an address ending in `.workers.dev`. The project folder already contains a file called `wrangler.jsonc`, which tells Cloudflare where the built site is. You do not need to change it.

To change the first part of the address, rename the project (the `name` in `wrangler.jsonc`, and the project name in the dashboard). The account part can be changed under **Workers & Pages** in the dashboard. To use your own address, such as `www.duballab.org`, register that domain and add it in the project's settings under **Domains & Routes**.

### 3.3 Keep the site private while it is being built (optional)

1. In Cloudflare, open **Zero Trust**, then **Access**, then **Applications**, then **Add an application**, then **Self-hosted**.
2. Enter the site's address as the application domain.
3. Add a policy with the action **Allow** that lists the email addresses allowed in.

Visitors then receive a one-time code by email. Delete the application when the site is ready to be public.

---

## 4. Everyday editing in the browser (no installs)

You only need a web browser and your GitHub login.

### 4.1 Edit people, publications and news with Pages CMS

1. Go to [pagescms.org](https://pagescms.org) and sign in with GitHub. The first time, allow it to access your `duballab` repository.
2. Open the `duballab` project. You see three collections: **People**, **Publications** and **News**.
3. Choose one, then **Add an entry** or open an existing entry. Fill in the form. Pictures can be uploaded straight from the form.
4. Choose **Save**. This saves the change to GitHub, and the live site updates within about two minutes.

### 4.2 Edit any other page with GitHub's built-in editor

Use this for the home page, About, Links, Positions, Contact, Donate, and for the site settings.

1. Open your repository on GitHub.
2. Click the folder `content`, then click the file you want (the list is in section 6.1).
3. Click the **pencil icon** (top right of the file) to edit.
4. Change the text. Keep the lines made of three dashes (`---`) exactly as they are.
5. Choose **Commit changes** (green button). Keep the default option, which saves to the main version.
6. Wait about two minutes. The live site updates.

### 4.3 Add a picture

1. In your repository, open the folder **`static`**, then **`images`** (or **`images/people`** for portraits).
2. Choose **Add file**, then **Upload files**, and drag the picture in.
3. Choose **Commit changes**.
4. Refer to the picture from a content file with a path that starts with `/images/`. See section 7.

### 4.4 Follow the build

To see whether the site rebuilt, or why it did not, open **Workers & Pages** in Cloudflare, open the project, and choose the **Deployments** tab. A green entry means success. A red entry shows the error: the live site keeps showing the last good version until the error is fixed.

---

## 5. Editing on your own computer (optional)

Working locally lets you **preview your changes privately before they go live**, and run the automatic checks. It needs a one-time installation. You do **not** need to know Git commands: GitHub Desktop does it with buttons.

### 5.1 One-time installation (Windows)

1. **GitHub Desktop** (copies the project and sends changes with buttons): download it from [desktop.github.com](https://desktop.github.com), install it, and sign in with your GitHub account.
2. **Hugo** (shows the site on your own computer). Open the **Start menu**, type **PowerShell**, open it, and run:

   ```powershell
   winget install --id Hugo.Hugo.Extended -e
   ```

   It must be the **extended** version. If `winget` is not available on your computer, download the file named `hugo_extended_..._windows-amd64.zip` from [github.com/gohugoio/hugo/releases](https://github.com/gohugoio/hugo/releases), unzip it, and put `hugo.exe` in a folder that is on your PATH.
3. **Close PowerShell and open a new one**, then check that it works:

   ```powershell
   hugo version
   ```

   It should print a version number that says `extended`.
4. **Python** is only needed for the automatic check in section 8. Install it from [python.org](https://www.python.org/downloads/) if you want that check.
5. On a Mac, use Homebrew instead: `brew install hugo`.

### 5.2 Copy the project to your computer

1. Open GitHub Desktop.
2. Choose **File, then Clone repository**. Pick your `duballab` repository from the list and choose a folder on your computer. Choose **Clone**.

### 5.3 See the site on your computer

1. In GitHub Desktop choose **Repository, then Open in Command Prompt** (or open PowerShell and go to the project folder).
2. Run:

   ```powershell
   hugo server
   ```

3. Open the address it prints (usually **http://localhost:1313/**). This is your private preview. Every time you save a file, the page refreshes.
4. Stop the preview with **Ctrl + C**.

### 5.4 Edit and publish

1. Edit the files with a text editor. [Visual Studio Code](https://code.visualstudio.com) is free and good for this, but Notepad is enough. Section 6 explains the files.
2. Check the result in the preview.
3. In GitHub Desktop, your changed files appear on the left. Type a short summary of what you did in the box **Summary** (for example "Add new postdoc"), then choose **Commit to main**.
4. Choose **Push origin** (top). The live site updates within about two minutes.
5. **At the start of each working day**, choose **Fetch origin** and then **Pull origin**, so you have the newest version.

If GitHub Desktop reports a "conflict", stop and ask the person who maintains the project instead of guessing.

---

## 6. How to write the content files

Every page is a text file inside the **`content`** folder. Each file has two parts:

```
---
title: Contact
---
The text of the page goes here.
```

- Between the two `---` lines is the **front matter**: short labelled facts written as `name: value`.
- Below it is the **text**, written in a very simple format called Markdown.

Keep the `---` lines, colons and quotation marks exactly as in the examples.

### 6.1 Which file is which page

| File | Page |
|---|---|
| `content/_index.md` | Home: mission text, rotating pictures, four tiles |
| `content/about.md` | Research, then About |
| `content/links.md` | Research, then Links |
| `content/positions.md` | Positions |
| `content/contact.md` | Contact |
| `content/donate.md` | Donate |
| `content/people/*.md` | People: one file per person |
| `content/publications/*.md` | Research, then Publications: one file per paper |
| `content/news/*.md` | Research, then News: one file per news item |
| `hugo.toml` | Site name and the Facebook and X addresses in the footer |

### 6.2 Markdown cheat sheet

| You type | You get |
|---|---|
| `**bold text**` | **bold text** |
| `*italic text*` | *italic text* |
| `[link text](https://example.org)` | a clickable link |
| `![Describe the picture](/images/name.jpg)` | a picture |
| A blank line | A new paragraph |
| Two spaces at the end of a line | A line break without a new paragraph |
| `1. First`, `2. Second` (each on its own line) | A numbered list |
| `- First`, `- Second` (each on its own line) | A bulleted list |

### 6.3 The home page

In `content/_index.md`, the paragraph under the second `---` is the mission statement. Text between double stars, like `**aging and neuroscience laboratory**`, appears in blue.

At the top of the same file:

- **`slides:`** the pictures that rotate above the mission statement. Each has an `image` (a file in `static/images`) and an `alt` (a short description).
- **`tiles:`** the four boxes under the mission statement. Each has a `title`, a `url` (where it leads) and an `image`.

### 6.4 A person

One file per person in `content/people/`. To add one, copy an existing file, give the copy a new name made of lowercase letters and dashes (for example `jane-doe.md`), and edit it. If you use Pages CMS, just fill in the form.

```
---
name: "Jane Doe, PhD"
title: "Postdoctoral Fellow"
email: "jane.doe@ucsf.edu"
photo: /images/people/jane-doe.jpg
order: 13
---
A short biography goes here.
```

- **name**: shown in bold. Keep one format: name, comma, degrees (for example `Uday Chockanathan, MD, PhD`).
- **title**: shown in italics under the email.
- **email**: shown under the name. Use `email: ""` to show none.
- **photo**: a roughly square portrait, see section 7.
- **order**: people are listed from the lowest number to the highest. Give someone the lowest number to put them first.
- The text under the second `---` is the biography. Use a blank line between paragraphs.

To remove a person, delete their file.

### 6.5 A publication

One file per paper in `content/publications/`:

```
---
title: "Title of the paper"
link: "https://doi.org/10.1000/example"
authors: "Doe J, Roe J, Dubal DB."
journal_line: "Aging Cell. 2018 Dec 17; doi: 10.1111/acel.12871."
date: 2018-12-17
---
```

- **link**: where the title leads, usually a DOI link. If you leave it out, the title is shown as plain text.
- **date**: year-month-day. The newest paper is listed first.
- Keep the double quotation marks around the text values.

### 6.6 A news item

One file per item in `content/news/`:

```
---
outlet: "The New York Times"
title: "Headline of the article"
link: "https://www.nytimes.com/..."
date: 2025-03-05
---
Two or three sentences from the article, shown under the headline.
```

- A "Read More >>" link is added automatically.
- The text under the second `---` is optional.
- The newest date is listed first. An item without a date is listed last.

### 6.7 The menu and the footer

- **Menu order**: each page file has a `weight` number in its front matter. Lower numbers come first.
- **Facebook and X links**: change the addresses under `[params]` in `hugo.toml`.
- **Site name**: the `title` line in `hugo.toml`.

---

## 7. Adding pictures

1. Prepare the picture:
   - Use **JPG** for photos. Make it no wider than about **1350 pixels**. For portraits, about **300 pixels** wide is enough. Very large files make the site slow.
   - Name it with lowercase letters, numbers and dashes only, with no spaces (for example `jane-doe.jpg`).
2. Put the file in **`static/images`** (portraits in **`static/images/people`**). Upload it through GitHub (section 4.3), Pages CMS, or by copying it into that folder on your computer.
3. Refer to it with a path that starts with `/images/`:
   - A person: `photo: /images/people/jane-doe.jpg`
   - In a page's text: `![Make a Gift](/images/make-a-gift.jpg)`
4. **Always write a short description of the picture** (called alt text). Screen readers read it aloud to blind visitors, and it is shown when a picture fails to load. In a page's text it is the part in the square brackets. For slides it is the `alt:` line, and for tiles the `title:` line. The automatic check in section 8 fails if a picture has no description.

---

## 8. Checking your work

The project has an automatic check that builds the whole site and makes sure that every page has a title and every picture has a description.

It needs the local setup from section 5 (Hugo and Python). In PowerShell, inside the project folder, run:

```powershell
python -m unittest tests.test_site
```

It prints `OK` if all is well. Otherwise it names the file that needs fixing.

To build the site by hand and look for errors:

```powershell
hugo --minify
```

This creates a folder called `public` containing the finished site. It is rebuilt whenever needed and is ignored by GitHub, so you never edit or upload it.

If you only use the browser workflow (section 4), the equivalent check is the **Deployments** tab in Cloudflare (section 4.4): a failed build shows up there and does not affect the live site.

---

## 9. Troubleshooting

| Problem | What to try |
|---|---|
| I changed something but the live site is the same | Wait two minutes. Check the **Deployments** tab in Cloudflare for a red entry. Then hard refresh the page with **Ctrl + F5**. |
| The Deployments tab shows a red entry | Open it and read the error. It names the file and line. Usually a missing `---`, quotation mark or colon. Compare with a similar file that works, or undo your last change on GitHub (open the file, choose **History**, and revert). |
| The menu or layout looks wrong after a change | Hard refresh with **Ctrl + F5**. Your browser may be showing an old stylesheet. |
| A picture does not show | Check that the file is in `static/images`, that the file name and capital letters match exactly, and that the path starts with `/images/`. |
| `hugo` is "not recognised" | Close PowerShell, open a new window. If it still fails, repeat section 5.1. |
| The preview address does not open | Make sure `hugo server` is still running and that you are in the project folder. |
| GitHub Desktop shows a "conflict" or refuses to push | Choose **Pull origin** first. If it still fails, ask the person who maintains the project. |
| I made a mistake and want to undo it | On GitHub, open the file, choose **History**, and open the earlier version you want. Every previous version is kept. |

---

## 10. What is where

```
duballab/
├── content/              All the text of the site (one file per page or item)
│   ├── _index.md         Home page: mission text, slides, tiles
│   ├── about.md          Research > About
│   ├── links.md          Research > Links
│   ├── positions.md      Positions page
│   ├── contact.md        Contact page
│   ├── donate.md         Donate page
│   ├── people/           One file per person
│   ├── publications/     One file per publication
│   └── news/             One file per news item
├── static/               Files copied to the site as they are
│   ├── images/           All pictures (portraits in images/people)
│   ├── fonts/            The heading font (League Gothic, free open licence)
│   └── style.css         Colours, sizes and layout of the whole site
├── layouts/              Page templates: how content is arranged on a page
├── hugo.toml             Site name, footer links, the Research menu entry
├── .pages.yml            Settings for the Pages CMS online editor
├── wrangler.jsonc        Settings Cloudflare uses to publish the site
├── tests/test_site.py    The automatic check (section 8)
└── .gitignore            Files that are never sent to GitHub
```

The site needs nothing but Hugo: there is no framework, no extra build tooling and no JavaScript. The home page slider and the phone menu are done entirely with CSS. For changes to the design, the files to edit are in `layouts/` and `static/style.css`; it is easiest to ask a web developer for help with those.
