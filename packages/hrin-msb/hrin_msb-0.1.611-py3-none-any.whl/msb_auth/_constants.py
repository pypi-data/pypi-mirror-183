AUTH_REQUEST_USER_FIELD = "user"
AUTH_REQUEST_PASSWORD_FIELD = "password"

DEFAULT_AUTHENTICATION_CLASSES = ('msb_auth.validators.JwtTokenValidator',)


class TokenConst:
	username_field = "username"
	userid_field = "id"
	user_email_field = "email"


class MsAuthConst:
	AUTH_VALIDATION_USER_VALUE = "token"
	AUTH_VALIDATION_AUTH_TYPE = "ms_sso"


class LdapAuthConst:
	pass


class JwtAuthConfig:
	TOKEN_USER_CLASS: str = 'msb_auth.TokenUser'
	USER_ID_CLAIM: str = 'id'

	USER_AUTHENTICATION_RULE: str = 'msb_auth._defaults.jwt_user_auth_rule'
	ALGORITHM: str = 'HS256'
	AUTH_HEADER_TYPES: str = ('Bearer',)
	AUTH_HEADER_NAME: str = 'HTTP_AUTHORIZATION'
	USER_ID_FIELD: str = 'userid'

	TOKEN_TYPE_CLAIM: str = 'token_type'
	SLIDING_TOKEN_REFRESH_EXP_CLAIM: str = 'refresh_exp'
	JTI_CLAIM: str = 'jti'
	ROTATE_REFRESH_TOKENS: bool = False
	BLACKLIST_AFTER_ROTATION: bool = False

	ACCESS_TOKEN_LIFETIME = 30
	REFRESH_TOKEN_LIFETIME = 1440
	SIGNING_KEY: str = ""
	VERIFYING_KEY: str = SIGNING_KEY
	AUDIENCE: str = None
	ISSUER: str = None
