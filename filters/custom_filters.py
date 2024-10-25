from pyrogram import filters


async def for_registration(_, __, query):
    return query.data == "registration"


async def for_authorization(_, __, query):
    return query.data == "authorization"


reg_filter = filters.create(for_registration)
auth_filter = filters.create(for_authorization)
