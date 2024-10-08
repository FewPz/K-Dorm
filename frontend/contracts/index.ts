import { initContract } from "@ts-rest/core";

// Contracts
import { taskContract } from "./task";
import { identificationKeyContract } from "./identification";
import { authenticationContract } from "./authentication";

const c = initContract();

export const contract = c.router({
  task: taskContract,
  identificationKey: identificationKeyContract,
  authentication: authenticationContract,
});
