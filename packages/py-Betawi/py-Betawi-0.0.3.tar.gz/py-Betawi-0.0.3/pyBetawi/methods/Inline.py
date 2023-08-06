from geezlibs.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from ..config import Var


class InlineBot(Var):
    async def inline_pmpermit(self, ids):
        pm_results = [
            (
                InlineQueryResultArticle(
                    title='PmPermit Geez-Pyro!',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text='Approve',
                                    callback_data=f'terima_{ids}',
                                ),
                                InlineKeyboardButton(
                                    text='Disapprove',
                                    callback_data=f'tolak_{ids}',
                                ),
                            ],
                            [
                                InlineKeyboardButton(
                                    text='Close',
                                    callback_data=f'close',
                                ),
                            ]
                        ]
                    ),
                    input_message_content=InputTextMessageContent(self.PERMIT_MSG),
                )
            )
        ]
        
        return pm_results
    
    async def approve_pmpermit(
        self,
        cb,
        user_ids,
        OLD_MSG,
    ):
        from ..dB.pmpermit_db import approve_user, is_approved

        if is_approved(user_ids):
            await cb.answer("Pengguna Ini Sudah Ada Di Database.", show_alert=True)
            return
        approve_user(user_ids)
        await cb.edit_message_text("Pesan Anda Diterima")
        if str(user_ids) in OLD_MSG:
            await OLD_MSG[str(user_ids)].delete()
        
    async def disapprove_pmpermit(
        self,
        cb,
        user_ids,
    ):
        from ..dB.pmpermit_db import disapprove_user, is_approved
        
        if not is_approved(user_ids):
            return await cb.answer("Pengguna Ini Tidak Ada Di Database")
        disapprove_user(user_ids)
        await cb.edit_message_text("Pesan Anda Ditolak")