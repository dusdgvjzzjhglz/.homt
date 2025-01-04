<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>个人简介</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
             color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        .profile-info {
          display: flex;
          align-items: center;
          margin-bottom: 20px;

        }
        .profile-info img{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-right: 20px;
            object-fit: cover; /* 保持图片比例不失真 */
        }
        ol {
             padding-left: 20px;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
          a:hover {
                text-decoration: underline;
        }

    </style>
</head>
<body>
    <div class="container">
      <h1>个人简介</h1>

        <div class="profile-info">
          <img src="path/to/your/avatar.jpg" alt="头像">  <!-- 这里替换你的头像路径 -->
          <ol>
            <li><strong>学号:</strong> 12345678</li>   <!-- 替换你的学号 -->
            <li><strong>姓名:</strong> 张三</li>   <!-- 替换你的姓名 -->
            <li><strong>手机号:</strong> 13812345678</li>    <!-- 替换你的手机号 -->
          </ol>
        </div>

      <p>
            大家好，我是一个热爱编程和技术的学生，喜欢探索新的知识，并将其应用到实际项目中。
            我正在努力学习 Python 编程，并希望能够使用它来解决实际问题。
            我同时也喜欢体育运动， 比如跑步和羽毛球。
        </p> <!--替换你的自我介绍-->
      
      <p>
        <a href="https://www.pythonanywhere.com">我的 PythonAnywhere 网站</a>
      </p>

    </div>
</body>
</html>
