from typing import List, Optional
from domain.entities.products import Product    
from domain.entities.orders import Order, Status
from domain.entities.users import User, ShippingAddress 
from domain.entities.payments import Payment, PaymentStatus
from domain.repositories.payment_repository import PaymentRepository
from domain.exceptions.payment_exceptions import PaymentNotFound


class PaymentService:
    def __init__(self, payment_repository: PaymentRepository):
        self.payment_repository = payment_repository


    async def create(self, payment : Payment) -> Payment:
        saved_payment = await self.payment_repository.save(payment)
        return saved_payment
    
    async def get_by_id(self, payment_id : int) -> Optional[Payment]:
        payment = await self.payment_repository.get_by_id(payment_id)
        if payment:
            return payment
        raise PaymentNotFound(f'Payment with id {payment_id} not found')
    


    async def mark_payment_completed(self, payment_id : int, status : PaymentStatus) -> Optional[Payment]:
        payment = await self.payment_repository.get_by_id(payment_id)
        if payment:
            payment.mark_payment(status)
            updated_payment = await self.payment_repository.update(payment)
            return updated_payment
        return PaymentNotFound(f'no payment with id {payment_id} found')
    
    async def delete(self, payment_id : int) -> None:
        payment = await self.payment_repository.get_by_id(payment_id)
        if payment:
            await self.payment_repository.delete(payment)
            return
        raise PaymentNotFound(f'Payment with id {payment_id} not found')
    

    async def list_all_payments(self) -> List[Payment]:
        payments = await self.payment_repository.list_all()
        return payments
    
    async def list_payment_by_user(self, user_id : int) -> List[Payment]:
        payments = await self.payment_repository.list_by_user(user_id)
        return payments
    
    async def search(self, term : str) -> Optional[Payment]:
        payments = await self.payment_repository.search(term)
        return payments
        