#vpi接口调用文档


URL Style | HTTP Method | Action| URL Name  
-|-|-|-  
{prefix}/	GET	list	{basename}-list
{prefix}/	POST	create	{basename}-list
{prefix}/{url_path}/	GET, or as specified by methods argument	@action(detail=False) decorated method	{basename}-{url_name}
{prefix}/{lookup}/	GET	retrieve	{basename}-detail
{prefix}/{lookup}/	PUT	update	{basename}-detail
{prefix}/{lookup}/	PATCH	partial_update	{basename}-detail
{prefix}/{lookup}/	DELETE	destroy	{basename}-detail
{prefix}/{lookup}/{url_path}/	GET, or as specified by methods argument	@action(detail=True) decorated method	{basename}-{url_name}


url | 描述 | 作用  
-|-|-  
http://host:port/users/ |  get/post | 更新或者修改用户表  
http://host:port/users/login/ |  post | 登录  
http://host:port/users/{pk}/ |  post | 更新或者修改用户表  
http://host:port/users/ |  get/post | 更新或者修改用户表
  