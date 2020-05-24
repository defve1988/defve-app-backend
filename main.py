from app import create_app

main = create_app()
dev = False
main.run(debug=dev)