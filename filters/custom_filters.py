from pyrogram import filters, types


async def for_registration(_, __, query) -> bool:
    return query.data == "registration"


async def for_authorization(_, __, query) -> bool:
    return query.data == "authorization"


def for_create_task(data: str):
    async def func(flt, _, message: types.Message):
        return flt.data.lower() == message.text.lower()

    return filters.create(func, data=data)

reg_filter = filters.create(for_registration)
auth_filter = filters.create(for_authorization)
