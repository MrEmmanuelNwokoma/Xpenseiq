import secrets
import string
from uuid import uuid4
from datetime import datetime, timezone, timedelta
from src.models.company import Company


class TokenUtils:
    def generate_key(self, length: int = 32):
        return secrets.token_hex(length)
    
    def generate_token(self, length: int = 6):
        return "".join(secrets.choice(string.digits) for _ in range(length))
    
    async def generate_company_verfication_token(self, company: Company, expiry_time: int = 3):
        token = self.generate_token()
        company.verification_token  = str(token)
        company.verification_token_expires_at = datetime.now(timezone.utc) + timedelta(minutes=expiry_time)
        return company.verification_token
    