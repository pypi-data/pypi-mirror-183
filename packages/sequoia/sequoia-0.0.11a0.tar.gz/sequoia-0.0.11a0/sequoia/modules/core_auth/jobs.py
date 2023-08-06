from sequoia.libs.jobs import JOBTASK


class TASK_FORGOT(JOBTASK):
    taskname = "forgot_password"


class TASK_LOGIN(JOBTASK):
    taskname = "login"


class TASK_UPDATE(JOBTASK):
    taskname = "update_profile"
