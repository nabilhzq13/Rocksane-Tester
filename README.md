# Rocksane Free

Point your phone at a bouldering wall, tap one hold of your route, and Rocksane finds the rest of that colour and shows the hand and foot moves to the top, on a climber drawn at your real size.

**Open it on your phone:** https://nabilhzq13.github.io/Rocksane-Tester/

This is the free version with everything unlocked, for testers. No purchase, no account, and nothing leaves your phone.

## What's included

Everything, including what is Rocksane Pro in the store app:

- Photos and the colour reader, real-size planning, every move with tips, and the Learn guide
- **Live camera**: point the phone at the wall and the moves appear
- **Record video**: film a clip and it reads the wall frame by frame
- **Hold type**: mark jugs, crimps, slopers and the rest; the plan and tips change
- All nine animated technique examples

## On your phone

1. Open the link above in Safari (iPhone) or Chrome (Android).
2. Tap the camera icon, then **Live camera** or **Take photo**. Stand back so the whole route fits, from the mats to the top of the wall. Allow camera access when asked.
3. Tap one hold of your route. The moves appear; tap **Play moves**, or the arrows to step through them.
4. To keep it on your home screen: Share → **Add to Home Screen**.

## Updating

This site is built from the main Rocksane source in [RockyMate](https://github.com/nabilhzq13/RockyMate). After changing Rocksane there:

```bash
python update.py PATH_TO_ROCKYMATE   # rebuilds and copies the unlocked edition here
git add -A && git commit -m "Update Rocksane Free" && git push
```

GitHub Pages serves this repository's `main` branch, so the link updates about a minute after the push.
