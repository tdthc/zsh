@echo off
DOSKEY ls=DIR $* 

DOSKEY ga=git add
DOSKEY gst=git status
DOSKEY gco=git checkout
DOSKEY gaa=git add --all
DOSKEY gcmsg=git commit -m
DOSKEY gcp=git cherry-pick
DOSKEY gcpc=git cherry-pick --continue
DOSKEY gcpa=git cherry-pick --abort
DOSKEY gapa=git add --patch
DOSKEY gau=git add --update
DOSKEY gav=git add --verbose
DOSKEY gap=git apply
DOSKEY gapt=git apply --3way