# FlagCounter Updater for osu! `!me`

This repo automatically fetches your FlagCounter image every 10 minutes, saves it as a static PNG, and serves it via GitHub Pages so osu! accepts it.

## Setup Steps
1. Create a new repo on your GitHub account named `flagcounter-updater`.
2. Upload these files to the repo.
3. Enable GitHub Pages in the repo settings (choose branch: `main`, folder: `/root`).
4. After a few minutes, your flag counter will be available at:
   https://Asp3ct109.github.io/flagcounter-updater/flagcounter.png
5. In osu! `!me` section, use:
   `[img]https://Asp3ct109.github.io/flagcounter-updater/flagcounter.png[/img]`

The workflow only commits when the image actually changes, so your commit history stays clean.
