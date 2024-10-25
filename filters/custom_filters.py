from pyrogram import filters


async def for_registration(_, __, query) -> bool:
    return query.data == "registration"


async def for_authorization(_, __, query) -> bool:
    return query.data == "authorization"


reg_filter = filters.create(for_registration)
auth_filter = filters.create(for_authorization)
