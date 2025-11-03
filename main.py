from dotenv import load_dotenv

from agent import agent


load_dotenv()

def main():
    print("=== Welcome to My Console App ===")

    while True:
        question = input("Enter your question: ").strip()
        response = agent.run(question)
        print(response.content)

if __name__ == "__main__":
    main()