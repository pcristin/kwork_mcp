# This file is auto-generated. Do not edit by hand.
# Regenerate with: python3 scripts/generate_openapi_mixin.py
from __future__ import annotations

from typing import Any, Protocol


class _OpenAPIClientProto(Protocol):
    async def request(
        self,
        method: str,
        endpoint: str,
        use_token: bool = False,
        _headers: dict[str, str] | None = None,
        _cookies: dict[str, str] | None = None,
        **params: Any,
    ) -> dict[str, Any]: ...
    async def request_with_body(
        self,
        endpoint: str,
        use_token: bool = False,
        _headers: dict[str, str] | None = None,
        _cookies: dict[str, str] | None = None,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]: ...
    async def request_multipart(
        self,
        endpoint: str,
        use_token: bool = False,
        _headers: dict[str, str] | None = None,
        _cookies: dict[str, str] | None = None,
        fields: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]: ...


class OpenAPIMethodsMixin(_OpenAPIClientProto):
    """Auto-generated wrappers for every endpoint from docs/openapi.json."""

    async def accept_extras(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /acceptExtras - Принятие предложенных опции в треке покупателем - auth: token+basic"""
        return await self.request("post", "acceptExtras", use_token=use_token, **params)

    async def accept_stage_suggestion(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /acceptStageSuggestion - Принятие встречного предложения этапов - auth: token+basic"""
        return await self.request("post", "acceptStageSuggestion", use_token=use_token, **params)

    async def actor(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /actor - Данные авторизованного пользователя - content: form - auth: token+basic"""
        return await self.request_with_body("actor", use_token=use_token, body=body, **params)

    async def add_favorite_categories(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /addFavoriteCategories - Изменение списка любимых категорий пользователя - auth: token+basic"""
        return await self.request("post", "addFavoriteCategories", use_token=use_token, **params)

    async def add_new_phone_number(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /addNewPhoneNumber - Проверка кода активации для добавления нового номера телефона на замену старому - auth: token+basic"""
        return await self.request("post", "addNewPhoneNumber", use_token=use_token, **params)

    async def add_phone_number(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /addPhoneNumber - Запрос кода для добавления номера телефона - auth: token+basic"""
        return await self.request("post", "addPhoneNumber", use_token=use_token, **params)

    async def add_stage(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /addStage - Создание и резервирование этапа в заказе - auth: token+basic"""
        return await self.request("post", "addStage", use_token=use_token, **params)

    async def allow_inbox_request(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /allowInboxRequest - Разрешить/не разрешить переписку с пользователем - auth: token+basic"""
        return await self.request("post", "allowInboxRequest", use_token=use_token, **params)

    async def allow_mobile_push(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /allowMobilePush - Устанавливает/снимает флаг разрешения отправки пуша в мобильное приложение - auth: token+basic"""
        return await self.request("post", "allowMobilePush", use_token=use_token, **params)

    async def allow_order_portfolio_upload(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /allowOrderPortfolioUpload - Разрешить продавцу публикацию работы в портфолио - auth: token+basic"""
        return await self.request(
            "post", "allowOrderPortfolioUpload", use_token=use_token, **params
        )

    async def allow_push_notifications_sound(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /allowPushNotificationsSound - Устанавливать / снимать флаг разрешения воспроизведения звука при отображении пуша в мобильном приложении. - auth: token+basic"""
        return await self.request(
            "post", "allowPushNotificationsSound", use_token=use_token, **params
        )

    async def apple_sign_in(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /appleSignIn - Аутентификация пользователя через Apple - content: form - auth: basic"""
        return await self.request_with_body("appleSignIn", use_token=use_token, body=body, **params)

    async def apply_filters(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /applyFilters - Установить выбранные фильтры продавца на бирже - auth: token+basic"""
        return await self.request("post", "applyFilters", use_token=use_token, **params)

    async def approve_order(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /approveOrder - Принятие заказа - auth: token+basic"""
        return await self.request("post", "approveOrder", use_token=use_token, **params)

    async def approve_order_stage(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /approveOrderStage - Принятие этапов заказа - auth: token+basic"""
        return await self.request("post", "approveOrderStage", use_token=use_token, **params)

    async def archive_dialog(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /archiveDialog - Отправить диалог в архив - auth: token+basic"""
        return await self.request("post", "archiveDialog", use_token=use_token, **params)

    async def block_dialog(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /blockDialog - Заблокировать диалог - auth: token+basic"""
        return await self.request("post", "blockDialog", use_token=use_token, **params)

    async def blocked_dialog_list(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /blockedDialogList - Список заблокированных для диалога юзеров - auth: token+basic"""
        return await self.request("post", "blockedDialogList", use_token=use_token, **params)

    async def cancel_order_awaiting_payment(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /cancelOrderAwaitingPayment - Удалить неоплаченный заказ - auth: token+basic"""
        return await self.request(
            "post", "cancelOrderAwaitingPayment", use_token=use_token, **params
        )

    async def cancel_order_by_payer(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /cancelOrderByPayer - Покупатель отменяет заказ - content: form - auth: token+basic"""
        return await self.request_with_body(
            "cancelOrderByPayer", use_token=use_token, body=body, **params
        )

    async def cancel_order_by_worker(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /cancelOrderByWorker - Продавец отменяет заказ - content: form - auth: token+basic"""
        return await self.request_with_body(
            "cancelOrderByWorker", use_token=use_token, body=body, **params
        )

    async def catalog_categories(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /catalogCategories - Получение списка подкатегорий - auth: basic"""
        return await self.request("post", "catalogCategories", use_token=use_token, **params)

    async def catalog_filters(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /catalogFilters - Список фильтров из текущего раздела каталога - auth: basic"""
        return await self.request("post", "catalogFilters", use_token=use_token, **params)

    async def catalog_main(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /catalogMain - Получение основной информации по главной странице каталога - auth: token+basic"""
        return await self.request("post", "catalogMain", use_token=use_token, **params)

    async def catalog_mainv2(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /catalogMainv2 - Получение основной информации по главной странице нового каталога - auth: basic"""
        return await self.request("post", "catalogMainv2", use_token=use_token, **params)

    async def catalog_rubrics(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /catalogRubrics - Рубрики меню - auth: basic"""
        return await self.request("post", "catalogRubrics", use_token=use_token, **params)

    async def categories(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /categories - Список категорий - auth: basic"""
        return await self.request("post", "categories", use_token=use_token, **params)

    async def category(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /category - Получить данные о заданной категории - auth: basic"""
        return await self.request("post", "category", use_token=use_token, **params)

    async def category_attributes(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /categoryAttributes - Получить дерево всех атрибутов для заданной категории - auth: basic"""
        return await self.request("post", "categoryAttributes", use_token=use_token, **params)

    async def change_password(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /changePassword - Запрос изменения пароля пользователя, с отправкой посылка кода подтверждения на почту - content: form - auth: token+basic"""
        return await self.request_with_body(
            "changePassword", use_token=use_token, body=body, **params
        )

    async def change_payer_sub_role(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /changePayerSubRole - Сменить дочернюю роль покупателя - auth: token+basic"""
        return await self.request("post", "changePayerSubRole", use_token=use_token, **params)

    async def change_username(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /changeUsername - Запрос изменения логина пользователя - content: form - auth: token+basic"""
        return await self.request_with_body(
            "changeUsername", use_token=use_token, body=body, **params
        )

    async def check_login(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /checkLogin - Запрос проверки занятости логина - content: form - auth: basic"""
        return await self.request_with_body("checkLogin", use_token=use_token, body=body, **params)

    async def check_uad_duplicate(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /checkUadDuplicate - Проверить дублирование идентификатора устройства UAD - auth: token+basic"""
        return await self.request("post", "checkUadDuplicate", use_token=use_token, **params)

    async def cities(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /cities - Получение списка городов страны - auth: basic"""
        return await self.request("post", "cities", use_token=use_token, **params)

    async def clear_filters(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /clearFilters - Сбросить выбранных фильтров продавца на бирже - auth: token+basic"""
        return await self.request("post", "clearFilters", use_token=use_token, **params)

    async def confirm_cancel_order_request_by_payer(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /confirmCancelOrderRequestByPayer - Покупатель соглашается на обоюдную отмену заказа - auth: token+basic"""
        return await self.request(
            "post", "confirmCancelOrderRequestByPayer", use_token=use_token, **params
        )

    async def confirm_cancel_order_request_by_worker(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /confirmCancelOrderRequestByWorker - Продавец соглашается на обоюдную отмену заказа - auth: token+basic"""
        return await self.request(
            "post", "confirmCancelOrderRequestByWorker", use_token=use_token, **params
        )

    async def countries(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /countries - Получение списка стран - auth: basic"""
        return await self.request("post", "countries", use_token=use_token, **params)

    async def create_answer(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /createAnswer - Создать ответ на отзыв - content: form - auth: token+basic"""
        return await self.request_with_body(
            "createAnswer", use_token=use_token, body=body, **params
        )

    async def create_kwork_complain(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /createKworkComplain - Создание жалобы на кворк - content: form - auth: token+basic"""
        return await self.request_with_body(
            "createKworkComplain", use_token=use_token, body=body, **params
        )

    async def create_portfolio(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /createPortfolio - Добавить портфолио - auth: basic"""
        return await self.request("post", "createPortfolio", use_token=use_token, **params)

    async def create_review(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /createReview - Создать отзыв - content: form - auth: token+basic"""
        return await self.request_with_body(
            "createReview", use_token=use_token, body=body, **params
        )

    async def create_stage(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /createStage - Добавление этапа в заказ - auth: token+basic"""
        return await self.request("post", "createStage", use_token=use_token, **params)

    async def del_favorite_categories(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /delFavoriteCategories - Удаление любимых категорий пользователя - auth: token+basic"""
        return await self.request("post", "delFavoriteCategories", use_token=use_token, **params)

    async def delete_account(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteAccount - Удаление своего аккаунта - auth: token+basic"""
        return await self.request("post", "deleteAccount", use_token=use_token, **params)

    async def delete_cancel_order_request_by_payer(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteCancelOrderRequestByPayer - Покупатель удалил свой запрос на обоюдную отмену заказа - auth: token+basic"""
        return await self.request(
            "post", "deleteCancelOrderRequestByPayer", use_token=use_token, **params
        )

    async def delete_cancel_order_request_by_worker(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteCancelOrderRequestByWorker - Продавец удалил свой запрос на обоюдную отмену заказа - auth: token+basic"""
        return await self.request(
            "post", "deleteCancelOrderRequestByWorker", use_token=use_token, **params
        )

    async def delete_cover(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteCover - Удаление обложки пользователя - auth: token+basic"""
        return await self.request("post", "deleteCover", use_token=use_token, **params)

    async def delete_kwork(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteKwork - Удаление своего кворка - auth: token+basic"""
        return await self.request("post", "deleteKwork", use_token=use_token, **params)

    async def delete_offer(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteOffer - Удаляет предложение к запросу на услугу на бирже - auth: token+basic"""
        return await self.request("post", "deleteOffer", use_token=use_token, **params)

    async def delete_order_note(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteOrderNote - Удалить заметку о заказе - auth: token+basic"""
        return await self.request("post", "deleteOrderNote", use_token=use_token, **params)

    async def delete_portfolio(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deletePortfolio - Удаление портфолио - auth: token+basic"""
        return await self.request("post", "deletePortfolio", use_token=use_token, **params)

    async def delete_review(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteReview - Удаление отзыва - auth: token+basic"""
        return await self.request("post", "deleteReview", use_token=use_token, **params)

    async def delete_stage(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteStage - Удаление этапа из заказа - auth: token+basic"""
        return await self.request("post", "deleteStage", use_token=use_token, **params)

    async def delete_user_note(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteUserNote - Удалить заметку о пользователе - auth: token+basic"""
        return await self.request("post", "deleteUserNote", use_token=use_token, **params)

    async def delete_want(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /deleteWant - Удаляет запрос на услугу на бирже - auth: token+basic"""
        return await self.request("post", "deleteWant", use_token=use_token, **params)

    async def dialogs(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /dialogs - Список диалогов - auth: token+basic"""
        return await self.request("post", "dialogs", use_token=use_token, **params)

    async def edit_answer(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /editAnswer - Редактировать отзыв - content: form - auth: token+basic"""
        return await self.request_with_body("editAnswer", use_token=use_token, body=body, **params)

    async def edit_portfolio(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /editPortfolio - Редактировать портфолио - auth: basic"""
        return await self.request("post", "editPortfolio", use_token=use_token, **params)

    async def edit_review(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /editReview - Редактировать отзыв - content: form - auth: token+basic"""
        return await self.request_with_body("editReview", use_token=use_token, body=body, **params)

    async def edit_stage(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /editStage - Редактирование этапов в заказе - auth: token+basic"""
        return await self.request("post", "editStage", use_token=use_token, **params)

    async def email_verification_letter(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /emailVerificationLetter - Запрос отправки письма подтверждения email - auth: token+basic"""
        return await self.request("post", "emailVerificationLetter", use_token=use_token, **params)

    async def exchange_info(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /exchangeInfo - Ключевая информации по бирже - auth: token+basic"""
        return await self.request("post", "exchangeInfo", use_token=use_token, **params)

    async def favorite_categories(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /favoriteCategories - Получение списка любимых рубрик пользователя. - auth: token+basic"""
        return await self.request("post", "favoriteCategories", use_token=use_token, **params)

    async def favorite_kworks(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /favoriteKworks - Список избранных кворков - auth: token+basic"""
        return await self.request("post", "favoriteKworks", use_token=use_token, **params)

    async def fcm_notifications_read(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /fcmNotificationsRead - Пометка сообщений FCM прочитанными в МП - auth: token+basic"""
        return await self.request("post", "fcmNotificationsRead", use_token=use_token, **params)

    async def fcm_notifications_received(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /fcmNotificationsReceived - Пометка сообщений FCM полученными в МП - auth: token+basic"""
        return await self.request("post", "fcmNotificationsReceived", use_token=use_token, **params)

    async def fcm_token_request_failed(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /fcmTokenRequestFailed - Регистрация токена Firebase Cloud Messaging - auth: token+basic"""
        return await self.request("post", "fcmTokenRequestFailed", use_token=use_token, **params)

    async def file_delete(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /fileDelete - Удаление загруженного файла - auth: token+basic"""
        return await self.request("post", "fileDelete", use_token=use_token, **params)

    async def file_upload(
        self,
        *,
        use_token: bool = False,
        fields: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /fileUpload - Загрузка файла из FILES["upload_files"] - content: multipart - auth: basic"""
        return await self.request_multipart(
            "fileUpload", use_token=use_token, fields=fields, files=files, **params
        )

    async def get_actor_info(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getActorInfo - Информация о текущем залогиненном пользователе - content: form - auth: token+basic"""
        return await self.request_with_body(
            "getActorInfo", use_token=use_token, body=body, **params
        )

    async def get_arbitration_reasons(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getArbitrationReasons - Получить список причин перевода в арбитраж - auth: token+basic"""
        return await self.request("post", "getArbitrationReasons", use_token=use_token, **params)

    async def get_available_features(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getAvailableFeatures - Информация о доступных функциях - auth: token+basic"""
        return await self.request("post", "getAvailableFeatures", use_token=use_token, **params)

    async def get_badges_info(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getBadgesInfo - Плучение информации для бейджей о количестве важных уведомлений - content: form - auth: token+basic"""
        return await self.request_with_body(
            "getBadgesInfo", use_token=use_token, body=body, **params
        )

    async def get_bill_refill_url(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getBillRefillUrl - Получить ссылку для Yescrow платежа - auth: token+basic"""
        return await self.request("post", "getBillRefillUrl", use_token=use_token, **params)

    async def get_captcha_status(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getCaptchaStatus - Требуется ли показать капчу при запросе сброса пароля - auth: token+basic"""
        return await self.request("post", "getCaptchaStatus", use_token=use_token, **params)

    async def get_channel_api(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getChannel - Получить идентификатор socket-канала текущего пользователя - auth: token+basic"""
        return await self.request("post", "getChannel", use_token=use_token, **params)

    async def get_company_details(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getCompanyDetails - Получение деталей о компании по ИНН - auth: basic"""
        return await self.request("post", "getCompanyDetails", use_token=use_token, **params)

    async def get_complain_categories(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getComplainCategories - Получение списка жалоб - auth: basic"""
        return await self.request("post", "getComplainCategories", use_token=use_token, **params)

    async def get_cookie(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getCookie - Получение куки для авторизованных по токену - auth: token+basic"""
        return await self.request("post", "getCookie", use_token=use_token, **params)

    async def get_current_versions(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getCurrentVersions - Возвращает список текущих версий мобильных приложений - auth: basic"""
        return await self.request("post", "getCurrentVersions", use_token=use_token, **params)

    async def get_custom_options_presets(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getCustomOptionsPresets - Получить спиок цен для кастомных опций и добавляемого срока - auth: token+basic"""
        return await self.request("post", "getCustomOptionsPresets", use_token=use_token, **params)

    async def get_dialog(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getDialog - Получить диалог по идентификатору собеседника - auth: token+basic"""
        return await self.request("post", "getDialog", use_token=use_token, **params)

    async def get_extras_available_for_order(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getExtrasAvailableForOrder - Получить опции, доступные для добавления в заказ - auth: token+basic"""
        return await self.request(
            "post", "getExtrasAvailableForOrder", use_token=use_token, **params
        )

    async def get_fishing_tutorial_questions(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getFishingTutorialQuestions - Список вопросов для опроса о мошенниках (код 116) - auth: token+basic"""
        return await self.request(
            "post", "getFishingTutorialQuestions", use_token=use_token, **params
        )

    async def get_hidden_kworks(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getHiddenKworks - Получить список скрытых пользователем кворков - auth: token+basic"""
        return await self.request("post", "getHiddenKworks", use_token=use_token, **params)

    async def get_in_app_notification(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getInAppNotification - Получение In-app уведомлений - auth: basic"""
        return await self.request("post", "getInAppNotification", use_token=use_token, **params)

    async def get_inbox_tracks(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getInboxTracks - Список сообщений (c треками) в диалоге - auth: token+basic"""
        return await self.request("post", "getInboxTracks", use_token=use_token, **params)

    async def get_kwork_answers(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getKworkAnswers - Получение FAQ по кворку - auth: basic"""
        return await self.request("post", "getKworkAnswers", use_token=use_token, **params)

    async def get_kwork_details(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getKworkDetails - Получение данных о кворке - auth: basic"""
        return await self.request("post", "getKworkDetails", use_token=use_token, **params)

    async def get_kwork_details_extra(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getKworkDetailsExtra - Получение данных о кворке - auth: basic"""
        return await self.request("post", "getKworkDetailsExtra", use_token=use_token, **params)

    async def get_kwork_links_table(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getKworkLinksTable - Получить данные по ссылкам кворка - auth: basic"""
        return await self.request("post", "getKworkLinksTable", use_token=use_token, **params)

    async def get_kwork_links_tablev2(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getKworkLinksTablev2 - Получить данные по ссылкам кворка - auth: basic"""
        return await self.request("post", "getKworkLinksTablev2", use_token=use_token, **params)

    async def get_kwork_portfolios(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getKworkPortfolios - Получить работы портфолио для кворка - auth: basic"""
        return await self.request("post", "getKworkPortfolios", use_token=use_token, **params)

    async def get_kwork_reviews(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getKworkReviews - Получить отзывы для кворка - auth: basic"""
        return await self.request("post", "getKworkReviews", use_token=use_token, **params)

    async def get_order_cancellation_reasons(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getOrderCancellationReasons - Получить список причин отмены заказа - auth: token+basic"""
        return await self.request(
            "post", "getOrderCancellationReasons", use_token=use_token, **params
        )

    async def get_order_details(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getOrderDetails - Получение детальной информации о заказе - auth: token+basic"""
        return await self.request("post", "getOrderDetails", use_token=use_token, **params)

    async def get_order_files(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getOrderFiles - Получить список файлов заказа - auth: token+basic"""
        return await self.request("post", "getOrderFiles", use_token=use_token, **params)

    async def get_order_header(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getOrderHeader - Обновление блоков кеша шапки заказа - auth: token+basic"""
        return await self.request("post", "getOrderHeader", use_token=use_token, **params)

    async def get_order_provided_data(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getOrderProvidedData - Предоставленные данные по заказу - auth: token+basic"""
        return await self.request("post", "getOrderProvidedData", use_token=use_token, **params)

    async def get_ordered_extras(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getOrderedExtras - Получение дополнительных опций, которые уже добавлены в заказ - auth: token+basic"""
        return await self.request("post", "getOrderedExtras", use_token=use_token, **params)

    async def get_payer_company_modal_url(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """GET /getPayerCompanyModalUrl - Получение ссылки на страницу покупателя с открытой модалкой регистрации Компании - auth: basic"""
        return await self.request("get", "getPayerCompanyModalUrl", use_token=use_token, **params)

    async def get_payment_methods(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getPaymentMethods - Получение способов оплаты и информации о сервисном сборе - auth: token+basic"""
        return await self.request("post", "getPaymentMethods", use_token=use_token, **params)

    async def get_security_user_data(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getSecurityUserData - Получения данных для экрана "Безопасность" - auth: token+basic"""
        return await self.request("post", "getSecurityUserData", use_token=use_token, **params)

    async def get_subscribers_statistics(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getSubscribersStatistics - Данные о динамике подписчиков на канале - auth: basic"""
        return await self.request("post", "getSubscribersStatistics", use_token=use_token, **params)

    async def get_tracks(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getTracks - Возвращает информацию о треках заказа - auth: token+basic"""
        return await self.request("post", "getTracks", use_token=use_token, **params)

    async def get_user_info(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getUserInfo - Получение информации о пользователе - auth: basic"""
        return await self.request("post", "getUserInfo", use_token=use_token, **params)

    async def get_users_last_order_info(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getUsersLastOrderInfo - Возвращает информацию по последнему выполненному заказу между пользователем и собеседником, в котором было хотя бы одно сообщение - auth: token+basic"""
        return await self.request("post", "getUsersLastOrderInfo", use_token=use_token, **params)

    async def get_voice_message_convert_status(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getVoiceMessageConvertStatus - Получить статус конвертации голосового сообщения - auth: token+basic"""
        return await self.request(
            "post", "getVoiceMessageConvertStatus", use_token=use_token, **params
        )

    async def get_voice_message_transcription(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getVoiceMessageTranscription - Получить транскрипцию голосового сообщения - auth: token+basic"""
        return await self.request(
            "post", "getVoiceMessageTranscription", use_token=use_token, **params
        )

    async def get_wants_count(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getWantsCount - Возвращает количество проектов по заданным фильтрам - auth: token+basic"""
        return await self.request("post", "getWantsCount", use_token=use_token, **params)

    async def get_web_auth_token(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /getWebAuthToken - Получить токен входа в веб версию - auth: token+basic"""
        return await self.request("post", "getWebAuthToken", use_token=use_token, **params)

    async def hide_dialog(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /hideDialog - Скрыть/удалить диалог - auth: token+basic"""
        return await self.request("post", "hideDialog", use_token=use_token, **params)

    async def hide_self_employed_notification(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /hideSelfEmployedNotification - Скрыть уведомление об успешной регистрации СЗ/ИП - auth: basic"""
        return await self.request(
            "post", "hideSelfEmployedNotification", use_token=use_token, **params
        )

    async def hide_voice_message_settings_popup(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /hideVoiceMessageSettingsPopup - Отправка на бэк факта показа попапа - auth: token+basic"""
        return await self.request(
            "post", "hideVoiceMessageSettingsPopup", use_token=use_token, **params
        )

    async def inbox_complain_message(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxComplainMessage - Пожаловаться на сообщение пользователя - content: form - auth: token+basic"""
        return await self.request_with_body(
            "inboxComplainMessage", use_token=use_token, body=body, **params
        )

    async def inbox_create(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxCreate - Создание нового сообщения - content: form - auth: token+basic"""
        return await self.request_with_body("inboxCreate", use_token=use_token, body=body, **params)

    async def inbox_custom_request_decline(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxCustomRequestDecline - Отмена индивидуального запроса - auth: token+basic"""
        return await self.request(
            "post", "inboxCustomRequestDecline", use_token=use_token, **params
        )

    async def inbox_delete(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxDelete - Удаление сообщения - auth: token+basic"""
        return await self.request("post", "inboxDelete", use_token=use_token, **params)

    async def inbox_edit(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxEdit - Редактирование сообщения - content: form - auth: token+basic"""
        return await self.request_with_body("inboxEdit", use_token=use_token, body=body, **params)

    async def inbox_forward(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxForward - Пересылка сообщения - auth: token+basic"""
        return await self.request("post", "inboxForward", use_token=use_token, **params)

    async def inbox_message(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxMessage - Получить сообщение Inbox по id - auth: token+basic"""
        return await self.request("post", "inboxMessage", use_token=use_token, **params)

    async def inbox_payer_decline(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxPayerDecline - Отмена предложенного кворка в личке покупателем - auth: token+basic"""
        return await self.request("post", "inboxPayerDecline", use_token=use_token, **params)

    async def inbox_read(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxRead - Пометить прочитанным сообщения или диалог - auth: token+basic"""
        return await self.request("post", "inboxRead", use_token=use_token, **params)

    async def inbox_track_message(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxTrackMessage - Получить сообщение Inbox/Track по conversationId - auth: token+basic"""
        return await self.request("post", "inboxTrackMessage", use_token=use_token, **params)

    async def inbox_worker_decline(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxWorkerDecline - Отмена предложенного кворка в личке продавцом - auth: token+basic"""
        return await self.request("post", "inboxWorkerDecline", use_token=use_token, **params)

    async def inboxes(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /inboxes - Список сообщений в диалоге - auth: token+basic"""
        return await self.request("post", "inboxes", use_token=use_token, **params)

    async def is_dialog_allow(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /isDialogAllow - Разрешен ли диалог с пользователем - auth: token+basic"""
        return await self.request("post", "isDialogAllow", use_token=use_token, **params)

    async def kworks(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /kworks - Список кворков для категории - auth: basic"""
        return await self.request("post", "kworks", use_token=use_token, **params)

    async def kworks_categories_list(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /kworksCategoriesList - Получение вкладок пользователя с категориями кворков - auth: basic"""
        return await self.request("post", "kworksCategoriesList", use_token=use_token, **params)

    async def kworks_status_list(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /kworksStatusList - Получение статусов (вкладок) кворков, и первую страницу самих кворков для каждого статуса - auth: token+basic"""
        return await self.request("post", "kworksStatusList", use_token=use_token, **params)

    async def logout(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /logout - Выход пользователя: удаление указанного пуш токена, удаление токена авторизации, закрытие текущей сессии - auth: token+basic"""
        return await self.request("post", "logout", use_token=use_token, **params)

    async def mark_inbox_tracks_as_read(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /markInboxTracksAsRead - Пометить переписку пользователя прочитанной - auth: token+basic"""
        return await self.request("post", "markInboxTracksAsRead", use_token=use_token, **params)

    async def mark_kwork_as_favorite(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /markKworkAsFavorite - Добавление кворка в избранные или удаление из избранных - auth: token+basic"""
        return await self.request("post", "markKworkAsFavorite", use_token=use_token, **params)

    async def mark_kwork_as_hidden(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /markKworkAsHidden - Скрытие/отображение кворка - auth: token+basic"""
        return await self.request("post", "markKworkAsHidden", use_token=use_token, **params)

    async def mark_kworks_black_friday(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /markKworksBlackFriday - Отмечает кворк участвующим в акции Черная пятница - auth: token+basic"""
        return await self.request("post", "markKworksBlackFriday", use_token=use_token, **params)

    async def mark_voice_message_heard(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /markVoiceMessageHeard - Отправить флаг "Пользователь прослушал голосовое сообщение" - auth: token+basic"""
        return await self.request("post", "markVoiceMessageHeard", use_token=use_token, **params)

    async def miniature(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /miniature - Получить миниатюру к файлу - auth: token+basic"""
        return await self.request("post", "miniature", use_token=use_token, **params)

    async def my_wants(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /myWants - Возвращает список запросов на услугу - auth: token+basic"""
        return await self.request("post", "myWants", use_token=use_token, **params)

    async def notifications(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /notifications - Список уведомлений пользователя - auth: token+basic"""
        return await self.request("post", "notifications", use_token=use_token, **params)

    async def notifications_fetch(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /notificationsFetch - Получение непрочитанных Push-событий из очереди - auth: token+basic"""
        return await self.request("post", "notificationsFetch", use_token=use_token, **params)

    async def notifications_received(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /notificationsReceived - Пометка сквозных Push-событий прочтенными - auth: token+basic"""
        return await self.request("post", "notificationsReceived", use_token=use_token, **params)

    async def offer(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /offer - Получает данные предложения к запросу на услугу на бирже - auth: token+basic"""
        return await self.request("post", "offer", use_token=use_token, **params)

    async def offer_order_options(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /offerOrderOptions - Добавить предложение опций к заказу - auth: token+basic"""
        return await self.request("post", "offerOrderOptions", use_token=use_token, **params)

    async def offers(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /offers - Предложения пользователя на запросы услуг на бирже - auth: token+basic"""
        return await self.request("post", "offers", use_token=use_token, **params)

    async def offline(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /offline - Установить статус offline - auth: token+basic"""
        return await self.request("post", "offline", use_token=use_token, **params)

    async def order(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /order - Информация о заказе - auth: token+basic"""
        return await self.request("post", "order", use_token=use_token, **params)

    async def order_kwork(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /orderKwork - Создать заказ по кворку. - auth: token+basic"""
        return await self.request("post", "orderKwork", use_token=use_token, **params)

    async def order_stage(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /orderStage - Зарезервировать этапы - auth: token+basic"""
        return await self.request("post", "orderStage", use_token=use_token, **params)

    async def orders_between(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /ordersBetween - Список активных заказов между текущим пользователем и указанным - auth: token+basic"""
        return await self.request("post", "ordersBetween", use_token=use_token, **params)

    async def pause_kwork(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /pauseKwork - Останавливает кворк - auth: token+basic"""
        return await self.request("post", "pauseKwork", use_token=use_token, **params)

    async def pay_order_awaiting_payment(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /payOrderAwaitingPayment - Оплата заказа в статусе "Ожидает оплаты" - auth: token+basic"""
        return await self.request("post", "payOrderAwaitingPayment", use_token=use_token, **params)

    async def payer_buy_extras(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /payerBuyExtras - Добавление опции в заказ покупателем - auth: token+basic"""
        return await self.request("post", "payerBuyExtras", use_token=use_token, **params)

    async def payer_decline_extras(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /payerDeclineExtras - Покупатель отклоняет предложенные опции - auth: token+basic"""
        return await self.request("post", "payerDeclineExtras", use_token=use_token, **params)

    async def payer_declines_extra_removal_request(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /payerDeclinesExtraRemovalRequest - Покупатель отклоняет запрос на удаление опции из заказа - auth: token+basic"""
        return await self.request(
            "post", "payerDeclinesExtraRemovalRequest", use_token=use_token, **params
        )

    async def payer_extra_delete(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /payerExtraDelete - Удалить опцию из заказа, для покупателя - auth: token+basic"""
        return await self.request("post", "payerExtraDelete", use_token=use_token, **params)

    async def payer_orders(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /payerOrders - Список заказов покупателя - auth: token+basic"""
        return await self.request("post", "payerOrders", use_token=use_token, **params)

    async def payer_upgrade_package(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /payerUpgradePackage - Апгрейд пакета покупателем - auth: token+basic"""
        return await self.request("post", "payerUpgradePackage", use_token=use_token, **params)

    async def portfolio_categories_list(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /portfolioCategoriesList - Получение категорий работ, и первой страницы самих работ для каждой категории - auth: token+basic"""
        return await self.request("post", "portfolioCategoriesList", use_token=use_token, **params)

    async def portfolio_list(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /portfolioList - Получить портфолио пользователя - auth: basic"""
        return await self.request("post", "portfolioList", use_token=use_token, **params)

    async def positive_reviews_count(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /positiveReviewsCount - Получить массив количества отзывов по атрибуту - auth: basic"""
        return await self.request("post", "positiveReviewsCount", use_token=use_token, **params)

    async def privacy(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /privacy - Вывод политики конфиденциальности - auth: basic"""
        return await self.request("post", "privacy", use_token=use_token, **params)

    async def project(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /project - Возвращает проект по идентификатору - auth: token+basic"""
        return await self.request("post", "project", use_token=use_token, **params)

    async def projects(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /projects - Возвращает список проектов по заданным фильтрам - auth: token+basic"""
        return await self.request("post", "projects", use_token=use_token, **params)

    async def push_in_app_notification_log(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /pushInAppNotificationLog - Запись лога показа in-app уведомления - auth: basic"""
        return await self.request("post", "pushInAppNotificationLog", use_token=use_token, **params)

    async def rate_arbitration(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /rateArbitration - Выставление оценки за арбитраж - auth: token+basic"""
        return await self.request("post", "rateArbitration", use_token=use_token, **params)

    async def recharge_balance(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /rechargeBalance - Получить ссылку для пополнения баланса в профиле и для создания заказа. - auth: token+basic"""
        return await self.request("post", "rechargeBalance", use_token=use_token, **params)

    async def register_cloud_token(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /registerCloudToken - Регистрация токена Firebase Cloud Messaging - auth: token+basic"""
        return await self.request("post", "registerCloudToken", use_token=use_token, **params)

    async def reject_cancel_order_request_by_payer(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /rejectCancelOrderRequestByPayer - Покупатель не согласился на обоюдную отмену заказа - auth: token+basic"""
        return await self.request(
            "post", "rejectCancelOrderRequestByPayer", use_token=use_token, **params
        )

    async def reject_cancel_order_request_by_worker(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /rejectCancelOrderRequestByWorker - Продавец не согласился на обоюдную отмену заказа - auth: token+basic"""
        return await self.request(
            "post", "rejectCancelOrderRequestByWorker", use_token=use_token, **params
        )

    async def reject_stage_suggestion(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /rejectStageSuggestion - Отмена встречного предложения этапов - auth: token+basic"""
        return await self.request("post", "rejectStageSuggestion", use_token=use_token, **params)

    async def repeat_order(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /repeatOrder - Создать заказ заново - auth: token+basic"""
        return await self.request("post", "repeatOrder", use_token=use_token, **params)

    async def replace_uad(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /replaceUad - Заменить идентификатор устройства UAD - auth: token+basic"""
        return await self.request("post", "replaceUad", use_token=use_token, **params)

    async def report_app_version(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /reportAppVersion - Обновление версии мобильного приложения пользователя - auth: token+basic"""
        return await self.request("post", "reportAppVersion", use_token=use_token, **params)

    async def request_phone_changing(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /requestPhoneChanging - Запрос кода для смены номера телефона - auth: token+basic"""
        return await self.request("post", "requestPhoneChanging", use_token=use_token, **params)

    async def reset_password(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /resetPassword - Отправка письма для сброса пароля - content: form - auth: token+basic"""
        return await self.request_with_body(
            "resetPassword", use_token=use_token, body=body, **params
        )

    async def resolution(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /resolution - Вывод политики разрешения споров - auth: basic"""
        return await self.request("post", "resolution", use_token=use_token, **params)

    async def restart_want(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /restartWant - Перезапускает запрос на услугу на бирже - auth: token+basic"""
        return await self.request("post", "restartWant", use_token=use_token, **params)

    async def save_order_note(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /saveOrderNote - Создать/редактировать заметку о заказе - content: form - auth: token+basic"""
        return await self.request_with_body(
            "saveOrderNote", use_token=use_token, body=body, **params
        )

    async def save_user_note(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /saveUserNote - Создать/редактировать заметку о пользователе - content: form - auth: token+basic"""
        return await self.request_with_body(
            "saveUserNote", use_token=use_token, body=body, **params
        )

    async def search(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /search - Поиск кворков - auth: basic"""
        return await self.request("post", "search", use_token=use_token, **params)

    async def search_dialogs(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /searchDialogs - Поиск диалогов - auth: token+basic"""
        return await self.request("post", "searchDialogs", use_token=use_token, **params)

    async def search_inboxes(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /searchInboxes - Поиск сообщенений в диалогах пользователей - auth: token+basic"""
        return await self.request("post", "searchInboxes", use_token=use_token, **params)

    async def search_kworks_catalog_query(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /searchKworksCatalogQuery - Получение ключевых слов по частичной фразе - auth: basic"""
        return await self.request("post", "searchKworksCatalogQuery", use_token=use_token, **params)

    async def search_messages(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /searchMessages - Поиск сообщенений в диалогах пользователей с указанием найденного сниппета - auth: token+basic"""
        return await self.request("post", "searchMessages", use_token=use_token, **params)

    async def search_order_tracks(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /searchOrderTracks - Поиск текстовых треков в заказе - auth: token+basic"""
        return await self.request("post", "searchOrderTracks", use_token=use_token, **params)

    async def search_tracks(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /searchTracks - Поиск текстовых треков в заказе - auth: token+basic"""
        return await self.request("post", "searchTracks", use_token=use_token, **params)

    async def send_bonus(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendBonus - Отправить бонус продавцу - auth: token+basic"""
        return await self.request("post", "sendBonus", use_token=use_token, **params)

    async def send_company_for_verification(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendCompanyForVerification - Отправка компании на проверку - auth: token+basic"""
        return await self.request(
            "post", "sendCompanyForVerification", use_token=use_token, **params
        )

    async def send_order_for_approval(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendOrderForApproval - Отправка заказа на проверку - auth: token+basic"""
        return await self.request("post", "sendOrderForApproval", use_token=use_token, **params)

    async def send_order_for_arbitration(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendOrderForArbitration - Отправить заказ на арбитраж - auth: token+basic"""
        return await self.request("post", "sendOrderForArbitration", use_token=use_token, **params)

    async def send_order_for_revision(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendOrderForRevision - Отправить заказ на доработку - auth: token+basic"""
        return await self.request("post", "sendOrderForRevision", use_token=use_token, **params)

    async def send_order_receipt_link_for_verification(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendOrderReceiptLinkForVerification - Отправка ссылки на чек для проверки - auth: token+basic"""
        return await self.request(
            "post", "sendOrderReceiptLinkForVerification", use_token=use_token, **params
        )

    async def send_order_requirements(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendOrderRequirements - Отправка информации по заказу продавцу - auth: token+basic"""
        return await self.request("post", "sendOrderRequirements", use_token=use_token, **params)

    async def send_report(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendReport - Отправить отчет по заказу (не этапному) - auth: token+basic"""
        return await self.request("post", "sendReport", use_token=use_token, **params)

    async def send_self_employed_survey_result(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendSelfEmployedSurveyResult - Отправить ответ на опрос - auth: token+basic"""
        return await self.request(
            "post", "sendSelfEmployedSurveyResult", use_token=use_token, **params
        )

    async def send_user_status(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendUserStatus - Отправить флаг "Статус пользователя" - auth: token+basic"""
        return await self.request("post", "sendUserStatus", use_token=use_token, **params)

    async def send_whats_app_code(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /sendWhatsAppCode - Отправить код верификации через WhatsApp - auth: token+basic"""
        return await self.request("post", "sendWhatsAppCode", use_token=use_token, **params)

    async def set_available_at_weekends(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setAvailableAtWeekends - Изменение доступности кворков на выходных - auth: token+basic"""
        return await self.request("post", "setAvailableAtWeekends", use_token=use_token, **params)

    async def set_dialog_starred(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setDialogStarred - Пометить диалог избранным - auth: token+basic"""
        return await self.request("post", "setDialogStarred", use_token=use_token, **params)

    async def set_favorite(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setFavorite - Изменение списка любимых категорий пользователя, объединяет функционал add и delete - auth: token+basic"""
        return await self.request("post", "setFavorite", use_token=use_token, **params)

    async def set_fishing_tutorial_status(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setFishingTutorialStatus - Установка статуса о прохождении опроса о мошенниках - auth: token+basic"""
        return await self.request("post", "setFishingTutorialStatus", use_token=use_token, **params)

    async def set_order_rating(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setOrderRating - Оценить продавца - auth: token+basic"""
        return await self.request("post", "setOrderRating", use_token=use_token, **params)

    async def set_taking_orders(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setTakingOrders - Сохранение настройки пользователя по доступности его кворков для заказа - auth: token+basic"""
        return await self.request("post", "setTakingOrders", use_token=use_token, **params)

    async def set_user_type(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setUserType - Установка типа пользователя (покупатель/продавец) - auth: token+basic"""
        return await self.request("post", "setUserType", use_token=use_token, **params)

    async def set_voice_message_receiving(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setVoiceMessageReceiving - Разрешить/запретить принимать голосовые сообщения - auth: token+basic"""
        return await self.request("post", "setVoiceMessageReceiving", use_token=use_token, **params)

    async def set_voice_message_speed(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /setVoiceMessageSpeed - Изменение скорости воспроизведения голосовых сообщений - auth: token+basic"""
        return await self.request("post", "setVoiceMessageSpeed", use_token=use_token, **params)

    async def sign_in(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /signIn - Аутентификация пользователя с выдачей токена - content: form - auth: basic"""
        return await self.request_with_body("signIn", use_token=use_token, body=body, **params)

    async def sign_up(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /signUp - Регистрация пользователя с выдачей токена - content: form - auth: basic"""
        return await self.request_with_body("signUp", use_token=use_token, body=body, **params)

    async def social_sign_in(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /socialSignIn - Аутентификация пользователя через социальные сети по коду провайдера - content: form - auth: basic"""
        return await self.request_with_body(
            "socialSignIn", use_token=use_token, body=body, **params
        )

    async def social_sign_in_by_token(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /socialSignInByToken - Аутентификация пользователя через токен социальной сети (при нативной авторизации моб. приложений)
        Аутентификация + регистрация
        (Устаревший метод, вскоре должен быть удален) - content: form - auth: basic"""
        return await self.request_with_body(
            "socialSignInByToken", use_token=use_token, body=body, **params
        )

    async def social_sign_in_by_tokenv2(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /socialSignInByTokenv2 - Аутентификация пользователя через токен социальной сети (при нативной авторизации моб. приложений) - content: form - auth: basic"""
        return await self.request_with_body(
            "socialSignInByTokenv2", use_token=use_token, body=body, **params
        )

    async def social_sign_up(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /socialSignUp - Регистрация через социальные сети с указанием email (привязка социального аккаунта если такой email уже есть) - content: form - auth: basic"""
        return await self.request_with_body(
            "socialSignUp", use_token=use_token, body=body, **params
        )

    async def social_sign_up_by_token(
        self,
        *,
        use_token: bool = False,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /socialSignUpByToken - Регистрация через социальные сети по токену с указанием email (привязка социального аккаунта если такой email уже есть) - content: form - auth: basic"""
        return await self.request_with_body(
            "socialSignUpByToken", use_token=use_token, body=body, **params
        )

    async def start_kwork(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /startKwork - Активирует(запускает) кворк - auth: token+basic"""
        return await self.request("post", "startKwork", use_token=use_token, **params)

    async def stop_want(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /stopWant - Останавливает запрос на услугу на бирже - auth: token+basic"""
        return await self.request("post", "stopWant", use_token=use_token, **params)

    async def suggest_stages(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /suggestStages - Встречное предложение этапов - auth: token+basic"""
        return await self.request("post", "suggestStages", use_token=use_token, **params)

    async def terms(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /terms - Вывод договора-оферты - auth: basic"""
        return await self.request("post", "terms", use_token=use_token, **params)

    async def terms_of_service(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /termsOfService - Вывод правил сайта - auth: basic"""
        return await self.request("post", "termsOfService", use_token=use_token, **params)

    async def timezones(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /timezones - Получение списка временных зон - auth: basic"""
        return await self.request("post", "timezones", use_token=use_token, **params)

    async def track_delete(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /trackDelete - Удаление трека - auth: token+basic"""
        return await self.request("post", "trackDelete", use_token=use_token, **params)

    async def track_edit(
        self,
        *,
        use_token: bool = True,
        body: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /trackEdit - Редактирование трека - content: form - auth: token+basic"""
        return await self.request_with_body("trackEdit", use_token=use_token, body=body, **params)

    async def track_message(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /trackMessage - Получить сообщение трека - auth: token+basic"""
        return await self.request("post", "trackMessage", use_token=use_token, **params)

    async def track_read(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /trackRead - Пометить указанные треки прочитанными - auth: token+basic"""
        return await self.request("post", "trackRead", use_token=use_token, **params)

    async def translation_languages(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /translationLanguages - Получить массив всех доступных в системе языков для переводов с падежами - auth: basic"""
        return await self.request("post", "translationLanguages", use_token=use_token, **params)

    async def typing(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /typing - Отправить флаг "Юзер печатает" - auth: token+basic"""
        return await self.request("post", "typing", use_token=use_token, **params)

    async def unarchive_dialog(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /unarchiveDialog - Вернуть диалог из архива - auth: token+basic"""
        return await self.request("post", "unarchiveDialog", use_token=use_token, **params)

    async def unblock_dialog(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /unblockDialog - Разблокировать диалог - auth: token+basic"""
        return await self.request("post", "unblockDialog", use_token=use_token, **params)

    async def unread_dialog(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /unreadDialog - Пометить диалог с заданным пользователем непрочитанным - auth: token+basic"""
        return await self.request("post", "unreadDialog", use_token=use_token, **params)

    async def update_avatar(
        self,
        *,
        use_token: bool = True,
        fields: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /updateAvatar - Смена аватара пользователя - content: multipart - auth: token+basic"""
        return await self.request_multipart(
            "updateAvatar", use_token=use_token, fields=fields, files=files, **params
        )

    async def update_chat_draft_message(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /updateChatDraftMessage - Обновление черновика - auth: token+basic"""
        return await self.request("post", "updateChatDraftMessage", use_token=use_token, **params)

    async def update_order_draft_message(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /updateOrderDraftMessage - Обновление черновика - auth: token+basic"""
        return await self.request("post", "updateOrderDraftMessage", use_token=use_token, **params)

    async def update_settings(
        self,
        *,
        use_token: bool = True,
        fields: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /updateSettings - Редактирование настроек пользователя - content: multipart - auth: token+basic"""
        return await self.request_multipart(
            "updateSettings", use_token=use_token, fields=fields, files=files, **params
        )

    async def update_stage_progress(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /updateStageProgress - Обновить прогресс по задаче - auth: token+basic"""
        return await self.request("post", "updateStageProgress", use_token=use_token, **params)

    async def upload_cover(
        self,
        *,
        use_token: bool = True,
        fields: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /uploadCover - Загрузка обложки пользователя - content: multipart - auth: token+basic"""
        return await self.request_multipart(
            "uploadCover", use_token=use_token, fields=fields, files=files, **params
        )

    async def upload_log(
        self,
        *,
        use_token: bool = False,
        fields: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /uploadLog - Загрузка лога мобильного приложения - content: multipart - auth: basic"""
        return await self.request_multipart(
            "uploadLog", use_token=use_token, fields=fields, files=files, **params
        )

    async def upload_portfolio_file(
        self,
        *,
        use_token: bool = False,
        fields: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /uploadPortfolioFile - Загрузка файла из FILES["file"] - content: multipart - auth: basic"""
        return await self.request_multipart(
            "uploadPortfolioFile", use_token=use_token, fields=fields, files=files, **params
        )

    async def uploaded_file(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /uploadedFile - Получение загруженного файла - auth: token+basic"""
        return await self.request("post", "uploadedFile", use_token=use_token, **params)

    async def user(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /user - Данные пользователя по идентификатору - auth: basic"""
        return await self.request("post", "user", use_token=use_token, **params)

    async def user_by_username(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /userByUsername - Получение данных пользователя по username - auth: basic"""
        return await self.request("post", "userByUsername", use_token=use_token, **params)

    async def user_kworks(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /userKworks - Список кворков пользователя - auth: token+basic"""
        return await self.request("post", "userKworks", use_token=use_token, **params)

    async def user_reviews(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /userReviews - Список отзывов для пользователя - auth: token+basic"""
        return await self.request("post", "userReviews", use_token=use_token, **params)

    async def user_search(
        self,
        *,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /userSearch - Поиск пользователей - auth: basic"""
        return await self.request("post", "userSearch", use_token=use_token, **params)

    async def verify_phone_activation_code(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /verifyPhoneActivationCode - Проверка кода активации номера телефона - auth: token+basic"""
        return await self.request(
            "post", "verifyPhoneActivationCode", use_token=use_token, **params
        )

    async def verify_sms_code_for_account_deleting(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /verifySmsCodeForAccountDeleting - Проверка кода удаления аккаунта - auth: token+basic"""
        return await self.request(
            "post", "verifySmsCodeForAccountDeleting", use_token=use_token, **params
        )

    async def viewed_catalog_kworks(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /viewedCatalogKworks - Список просмотренных кворков - auth: token+basic"""
        return await self.request("post", "viewedCatalogKworks", use_token=use_token, **params)

    async def voice_upload(
        self,
        *,
        use_token: bool = False,
        fields: dict[str, Any] | None = None,
        files: dict[str, Any] | None = None,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /voiceUpload - Загрузка файла из FILES["upload_files"] - content: multipart - auth: basic"""
        return await self.request_multipart(
            "voiceUpload", use_token=use_token, fields=fields, files=files, **params
        )

    async def want(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /want - Возвращает данные по запросу на услугу - auth: token+basic"""
        return await self.request("post", "want", use_token=use_token, **params)

    async def wants_status_list(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /wantsStatusList - Список запросов на услугу на бирже, сгруппированных по альтернативному статусу - auth: token+basic"""
        return await self.request("post", "wantsStatusList", use_token=use_token, **params)

    async def worker_confirms_extra_removal_request(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /workerConfirmsExtraRemovalRequest - Продавец подтверждает запрос на удаление опции - auth: token+basic"""
        return await self.request(
            "post", "workerConfirmsExtraRemovalRequest", use_token=use_token, **params
        )

    async def worker_decline_extras(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /workerDeclineExtras - Продавец отклоняет предложенные опции - auth: token+basic"""
        return await self.request("post", "workerDeclineExtras", use_token=use_token, **params)

    async def worker_declines_extra_removal_request(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /workerDeclinesExtraRemovalRequest - Продавец отклоняет запрос на удаление опции из заказа - auth: token+basic"""
        return await self.request(
            "post", "workerDeclinesExtraRemovalRequest", use_token=use_token, **params
        )

    async def worker_extra_delete(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /workerExtraDelete - Удалить опцию из заказа, для продавца - auth: token+basic"""
        return await self.request("post", "workerExtraDelete", use_token=use_token, **params)

    async def worker_inprogress(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /workerInprogress - Продавец взял заказ в работу - auth: token+basic"""
        return await self.request("post", "workerInprogress", use_token=use_token, **params)

    async def worker_orders(
        self,
        *,
        use_token: bool = True,
        **params: Any,
    ) -> dict[str, Any]:
        """POST /workerOrders - Список заказов пользователя, которые он должен выполнить - auth: token+basic"""
        return await self.request("post", "workerOrders", use_token=use_token, **params)
