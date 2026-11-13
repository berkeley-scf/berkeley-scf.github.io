---
title: Shared Hugging Face Hub Cache
---

As for November 17, 2026, the SCF has set up a shared cache directory for Hugging Face repositories (models, datasets, spaces). This has two purposes: (1) to reduce disk space used in redundantly storing models in user-specific directories and (2) to reduce download times by relying on cached files.

By default any model that is downloaded on your behalf will be saved to `/shared/huggingface/hub`, which is a directory available to all SCF machines and all users. The downloaded model will be available to other users as of 3 am that night. So the next user who tries to use that model will make use of the already cached materials and no new download will be needed (unless the next user needs files not downloaded by the initial user, in which case the additional files will automatically be downloaded to the shared cache directory).

If you prefer to have your own cache directory, you should set the environment variable `HF_HUB_CACHE` to the directory you want to use (in place of its default value of `/shared/huggingface/hub`). For example, you might want the directory to be on local disk on the machine you are working on. You can set `HF_HUB_CACHE` in your `.bashrc` if you'd like it always set in your sessions.

Finally, there is one limitation of how we have configured this. If one user downloads a model during one day and a second user tries to use the same model that same day before 3 am, they will get a permission denied error. This is because our nightly automated process that makes a model accessible to all other users runs at 3 am each night. If you encounter this error, as a temporary work-around for that day only, you can temporarily set `HF_HUB_CACHE` as described above to a directory that you own. Note that if you pick up your work the next day you should be able to use the shared cache directory (and in that case it would be best if you delete the model from your personal directory to save space). If this happens frequently to you, please let us know so that we can run our automated process more frequently than once per day to reduce how often this happens.

If you encounter any problems, please let us know.
