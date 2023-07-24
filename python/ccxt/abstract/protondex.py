from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_markets_all = publicGetMarketsAll = Entry('markets/all', 'public', 'GET', {})
    public_get_orders_open = publicGetOrdersOpen = Entry('orders/open', 'public', 'GET', {})
    public_get_orders_history = publicGetOrdersHistory = Entry('orders/history', 'public', 'GET', {})
    public_get_orders_lifecycle = publicGetOrdersLifecycle = Entry('orders/lifecycle', 'public', 'GET', {})
    public_get_orders_depth = publicGetOrdersDepth = Entry('orders/depth', 'public', 'GET', {})
    public_get_trades_daily = publicGetTradesDaily = Entry('trades/daily', 'public', 'GET', {})
    public_get_trades_history = publicGetTradesHistory = Entry('trades/history', 'public', 'GET', {})
    public_get_trades_recent = publicGetTradesRecent = Entry('trades/recent', 'public', 'GET', {})
    public_get_chart_ohlcv = publicGetChartOhlcv = Entry('chart/ohlcv', 'public', 'GET', {})
    public_get_status_sync = publicGetStatusSync = Entry('status/sync', 'public', 'GET', {})
    public_get_account_balances = publicGetAccountBalances = Entry('account/balances', 'public', 'GET', {})
    public_post_orders_serialize = publicPostOrdersSerialize = Entry('orders/serialize', 'public', 'POST', {})
    public_post_orders_submit = publicPostOrdersSubmit = Entry('orders/submit', 'public', 'POST', {})
    private_get_user_fees = privateGetUserFees = Entry('user/fees', 'private', 'GET', {})
    private_get_account_deposits = privateGetAccountDeposits = Entry('account/deposits', 'private', 'GET', {})
    private_get_account_withdrawals = privateGetAccountWithdrawals = Entry('account/withdrawals', 'private', 'GET', {})
