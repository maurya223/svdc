# TODO

- [ ] Fix production staticfiles 500: "Missing staticfiles manifest entry for 'img/logo.png'".
  - [x] Updated `clinic/settings.py` to use WhiteNoise `CompressedStaticFilesStorage` (no manifest) so missing manifest entries won’t crash requests.
  - [ ] (Optional but recommended) Ensure `static/` contains `img/logo.png` or move/copy the logo into `static/img/` and re-run `collectstatic` during build.
- [ ] Rebuild Docker image and redeploy.
- [ ] Verify `/` loads successfully on the deployed URL.

