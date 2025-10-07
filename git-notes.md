# Git Notes

## Create private ToddBooth repository
gh repo create cr-test --private

## Create private TeacherTodd repository
gh repo create teachertodd/cr-test --private

## Change to remote TeacherTodd
git remote -v
git remote set-url origin git@github.com:teachertodd/cr-test.git

## Change visability from private to public
gh repo edit teachertodd/cr-test --visibility public --accept-visibility-change-consequences

