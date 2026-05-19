
<template>
    <div class="content">
        <div class="main_block">
            <div class="form_block">
                <H1>Форма обратной связи</H1>
                <form>
                    <label for="email">Почта для ответа:</label>
                    <input type="email" id="email" name="email" placeholder="Ваш email" required>
                    
                    <label for="feedback">Ваше сообщение:</label>
                    <textarea id="feedback" name="text_feedback" placeholder="Напишите ваше сообщение здесь..." required></textarea>
                    
                    <button type="submit" class="submit-btn">Отправить</button>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
    body {
        margin: 0px;
        padding: 0px;
        font-family: 'MyFont', sans-serif;
        overflow-x: hidden;
        background-color: #f5f5f5;
    }

    h1 {
        font-weight: bold;
        font-size: 60px;
        text-align: center;
        margin-bottom: 40px;
        color: #2c3e50;
    }

    .content {
        width: 100vw;
        min-height: calc(100vh - 250px);
        background-color: #FFFFFF;
        padding: 50px 0;
    }

    .main_block {
        max-width: 1200px;
        margin: 0 auto;
        margin-top: 100px;
        padding: 0 20px;
        height: 100vh;
    }

    .form_block {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        padding: 40px;
        max-width: 800px;
        margin: 0 auto;
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 25px;
    }

    label {
        font-size: 18px;
        font-weight: 500;
        color: #34495e;
    }

    input[type="email"] {
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 16px;
        transition: border 0.3s;
    }

    textarea {
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 16px;
        min-height: 200px;
        resize: vertical;
        transition: border 0.3s;
        font-family: inherit;
    }

    .submit-btn {
        background-color: #2c3e50;
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 18px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        align-self: flex-start;
    }

    .submit-btn:hover {
        background-color: #3498db;
    }

    .footer {
        padding-top: 50px;
        padding-left: 50px;
        background-color: #141A20;
        font-size: 16px;
        display: flex;
        height: 200px;
        color: aliceblue;
        justify-content: space-around;
    }

    a {
        color: aliceblue;
        text-decoration: none;
        transition: color 0.3s;
    }

    a:hover {
        color: #3498db;
    }

    @media (max-width: 768px) {
        h1 {
            font-size: 40px;
        }
        
        .form_block {
            padding: 20px;
        }
        
        .footer {
            flex-direction: column;
            height: auto;
            padding: 30px;
            gap: 20px;
        }
    }

</style>