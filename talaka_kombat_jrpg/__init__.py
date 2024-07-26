from flask import Flask, request, jsonify

from talaka_kombat_jrpg.model.fight_simulator import FightSimulator


def create_app():
    app = Flask(__name__)

    @app.route("/simulate_fight", methods=["POST"])
    def fight_simulation():
        try:
            fight_data = request.get_json()

            if not fight_data or not isinstance(fight_data, dict):
                return jsonify({"error": "Invalid fight data provided."}), 400

            result = FightSimulator().start_fight(fight_data)

            return jsonify(
                {
                    "winner": result.winner.player_name,
                    "history": result.history,
                }
            ), 200

        except Exception as e:
            app.logger.error(f"Error during fight simulation: {str(e)}")
            return jsonify({"error": "Internal server error."}), 500

    return app
